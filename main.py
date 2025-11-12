import asyncio
import base64
import json
import logging
import os
from pathlib import Path

import numpy as np
import polars as po
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse


logger = logging.getLogger(__name__)
app = FastAPI()


def ensure_codex_auth_file() -> bool:
    """Reconstruct ~/.codex/auth.json from CODEX_AUTH_JSON_B64 when provided."""
    encoded = os.getenv("CODEX_AUTH_JSON_B64")
    if not encoded:
        logger.warning("CODEX_AUTH_JSON_B64 is not set; Codex CLI features will be disabled.")
        return False

    try:
        decoded = base64.b64decode(encoded)
        parsed = json.loads(decoded.decode("utf-8"))
    except Exception as exc:  # noqa: BLE001 - We want to log any failure during decoding/parsing.
        logger.error("Failed to decode CODEX_AUTH_JSON_B64: %s", exc)
        return False

    codex_dir = Path.home() / ".codex"
    auth_path = codex_dir / "auth.json"
    codex_dir.mkdir(parents=True, exist_ok=True)
    auth_path.write_text(json.dumps(parsed, indent=2), encoding="utf-8")
    os.chmod(auth_path, 0o600)
    logger.info("Codex auth.json restored to %s", auth_path)
    return True


def codex_session_dir(year: int, month: int, day: int) -> Path:
    return Path.home() / ".codex" / "session" / f"{year:04d}" / f"{month:02d}" / f"{day:02d}"


@app.on_event("startup")
async def startup_event() -> None:
    ensure_codex_auth_file()


@app.get("/")
async def top_page():
    return {"message": "Anything is in here...Now time"}


@app.post("/tasks")
async def task_generator():
    pass


async def task_compiler(task_id, llm_response, SSR_Model):
    pass


@app.get("/codex/sessions/{year}/{month}/{day}")
async def list_codex_sessions(year: int, month: int, day: int):
    session_path = codex_session_dir(year, month, day)
    if not session_path.exists():
        raise HTTPException(status_code=404, detail="Session directory not found")

    files = sorted(p.name for p in session_path.glob("*.jsonl") if p.is_file())
    return {"files": files}


@app.get("/codex/sessions/{year}/{month}/{day}/{filename}")
async def download_codex_session(year: int, month: int, day: int, filename: str):
    if Path(filename).name != filename:
        raise HTTPException(status_code=400, detail="Invalid filename")

    session_path = codex_session_dir(year, month, day)
    file_path = session_path / filename

    if not file_path.exists() or not file_path.is_file():
        raise HTTPException(status_code=404, detail="Session file not found")

    return FileResponse(file_path)
