#!/bin/bash
set -euo pipefail

TODAY=$(date +%F)
PYTHON="/opt/homebrew/opt/python@3.11/libexec/bin/python3"
CONTENT_FACTORY="$HOME/openclaw/skills/content-factory/scripts/run_content_factory.py"
OUT_DIR="$HOME/openclaw-work/out/articles/$TODAY"
POST_DIR="$HOME/openclaw-work/site/content/posts"

# 1. 生成文章
"$PYTHON" "$CONTENT_FACTORY" --client demo --date "$TODAY"

# 2. 复制到 Hugo，文件名加日期，避免覆盖
mkdir -p "$POST_DIR"
for f in "$OUT_DIR"/*.md; do
  [ -e "$f" ] || continue
  base="$(basename "$f")"
  cp "$f" "$POST_DIR/${TODAY}-${base}"
done

# 3. 提交并推送
cd "$HOME/openclaw-work/site"
git add content/posts publish.sh
git commit -m "auto publish $TODAY" || echo "No new changes"
git push
