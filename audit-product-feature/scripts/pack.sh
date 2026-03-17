#!/bin/bash
# scripts/pack.sh — pack target project trước khi audit
#
# Usage:
#   bash scripts/pack.sh /path/to/project
#   bash scripts/pack.sh /path/to/project my-project-name
#
# Output: output/context.xml (repomix packed file)

set -e

PROJECT_PATH=${1:?"Usage: bash scripts/pack.sh /path/to/project [name]"}
PROJECT_NAME=${2:-$(basename "$PROJECT_PATH")}
OUTPUT_DIR="output"

mkdir -p "$OUTPUT_DIR"

echo "Project : $PROJECT_NAME"
echo "Path    : $PROJECT_PATH"
echo "Output  : $OUTPUT_DIR/context.xml"
echo ""

# Check repomix
if ! command -v repomix &>/dev/null; then
  echo "repomix chưa cài. Đang cài..."
  npm install -g repomix
fi

repomix \
  --input "$PROJECT_PATH" \
  --output "$OUTPUT_DIR/context.xml" \
  --ignore "node_modules,dist,.git,*.lock,*.log,coverage,.env*" \
  --include "**/*.md,**/*.ts,**/*.js,**/*.py,**/*.json,src/**,docs/**,app/**"

echo ""
echo "Done. Context đã lưu vào $OUTPUT_DIR/context.xml"
echo "Giờ chạy Claude Code với: claude --add-dir $PROJECT_PATH"
