# 要求
- 論文「LLMs Reproduce Human Purchase Intent via Semantic Similarity Elicitation of Likert Ratings」（`./2510.08338v1.pdf`）に基づき、GPT-5モデルをCodex CLI経由で呼び出してSSR（Semantic Similarity Rating）比較を行うWebアプリケーションを実装する。
- SSRライブラリのリファレンス実装として https://github.com/pymc-labs/semantic-similarity-rating を採用する。
- Codex CLIの`codex exec`を利用してGPT-5を操作する。
- **本プロジェクトではSSR分析をマーケティング戦略（キャンペーン施策、プロダクト・ポジショニングなど）の評価に転用することが最重要課題である。** ペルソナやリファレンス文の設計、レポート指標はマーケティング・インサイトの抽出に直結するよう設計すること。
- Codex CLIの認証情報は環境変数`CODEX_AUTH_JSON_B64`（`~/.codex/auth.json`をBase64化した値）から復元すること。アプリケーション起動時に`~/.codex/auth.json`を自動生成し、権限を`600`に設定する。

Codex Exec Example:
```bash
codex exec --model gpt-5 --json --sandbox read-only --skip-git-repo-check "<Question Here>"
```

# 仕様
- バックエンドはFastAPIを用い、Codex execに対するジョブ管理、ペルソナ群の保存、結果レポート生成を行う。
- フロントエンドはNext.jsを用いる。
- 要求されるポイント
  - Codex execは同期的なので、FastAPIバックエンド側でジョブを管理し、タイムアウトやリトライ、キューイングを設計する。
  - Web UIから、ペルソナや戦略をどのようにプロンプトへ挿入するか調整できる。
  - SSR比較に用いる語群テーブルやリファレンス文セットの調整機能を提供する。
  - 各戦略ごとの結果レポートでは、ペルソナ年代別の平均評価、分布、相関・KS距離などの統計指標をグラフ化し、画像またはPDFでダウンロードできるようにする。
  - ペルソナ（年代・性別等）を管理する機能を実装する。
  - マーケティング用途での有効性を測定するため、キャンペーン別・施策別の比較やA/B指標との携を考慮したデータスキーマと可視化を用意する。
  - Codex CLIのセッションログ（`~/.codex/session/<Year>/<Month>/<Day>/*.jsonl`）を一覧化・ダウンロードできるAPIを実装し、UIから取得できるようにする。

# チェックリスト
- [ ] Codex CLIのセットアップと接続確認
- [ ] FastAPIバックエンドの仮想環境構築
- [ ] SSRライブラリを用いた試験pmf生成
- [ ] Next.jsフロントエンドの初期化とAPI疎通確認
- [ ] マーケティング評価指標（例：購入意向スコア、ブランド想起）へのマッピング設計
- [ ] `CODEX_AUTH_JSON_B64`を使った認証情報復元処理の実装とテスト
- [ ] CodexセッションログダウンロードAPIの実装とテスト

# 更新ログ / 開発での知見
- 2024-XX-XX: AGENTS.mdを初期整備。マーケティング戦略評価への転用を最重要課題として明記。
- 2024-XX-XX: Codex認証情報の環境変数復元方針とセッションログダウンロード要件を追記。

# テスト
- 適切な方法で実施し、結果をここに記録すること。

# その他
- 必要に応じて項目を追加し、このAGENTS.mdを思考の参照エンジンとして活用しながら実装を進めること。
