# Semantic Similarity Rating via Codex CLI

This project recreates the Semantic Similarity Rating (SSR) pipeline described in “LLMs Reproduce Human Purchase Intent via Semantic Similarity Elicitation of Likert Ratings” while adapting the insights to marketing-strategy evaluation workflows. The stack combines a FastAPI backend for Codex CLI orchestration with a Next.js frontend for persona, prompt, and analytics management.

## Codex CLI authentication

The FastAPI application expects Codex credentials to be delivered through the `CODEX_AUTH_JSON_B64` environment variable. The value must be the Base64-encoded contents of `~/.codex/auth.json` (the file produced after running `codex login`). A helper routine rebuilds `~/.codex/auth.json` on startup so that the CLI can run inside containers where the home directory begins empty.

1. Save your `auth.json` locally after authenticating with Codex CLI.
2. Encode it as a single-line Base64 string:
   - Linux (GNU `base64`):
     ```bash
     base64 -w0 ~/.codex/auth.json
     ```
   - macOS (BSD `base64`, which reads from stdin unless `-i` is provided):
     ```bash
     base64 -i ~/.codex/auth.json | tr -d '\n'
     ```
3. Export the value before running the application:
   ```bash
   export CODEX_AUTH_JSON_B64="<BASE64_ENCODED_AUTH_JSON>"
   ```

The backend will create the `~/.codex/auth.json` file with `0600` permissions. If the variable is missing or cannot be decoded, Codex features are disabled and a warning is logged.

### Sample `auth.json`

For reference, a truncated structure looks like:

```json
{
  "OPENAI_API_KEY": null,
  "tokens": {
    "id_token": "<JWT>",
    "access_token": "<JWT>",
    "refresh_token": "<REFRESH_TOKEN>",
    "account_id": "<ACCOUNT_UUID>"
  },
  "last_refresh": "2025-11-10T05:58:13.072481Z"
}
```

## Codex session archives

Every `codex exec` invocation stores a JSONL transcript under `~/.codex/sessions/<Year>/<Month>/<Day>/` (recent CLI builds use the plural `sessions`; older ones may still use `session/`). The backend exposes endpoints to list and download these artifacts so that operators can audit or re-use model outputs. Ensure the application container has read access to these directories.

## Development checklist

Follow the implementation checklist in [`AGENTS.md`](./AGENTS.md) to stay aligned with marketing evaluation goals, persona tooling, and analytics requirements.
