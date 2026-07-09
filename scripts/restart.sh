#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PID_FILE="$ROOT_DIR/backend.pid"
LOG_FILE="$ROOT_DIR/backend.log"
PORT="13144"

if [[ -f "$PID_FILE" ]]; then
  OLD_PID="$(cat "$PID_FILE")"
  if [[ -n "${OLD_PID}" ]] && kill -0 "$OLD_PID" 2>/dev/null; then
    kill "$OLD_PID" || true
    sleep 1
  fi
  rm -f "$PID_FILE"
fi

nohup python -m uvicorn backend.main:app --app-dir "$ROOT_DIR" --host 0.0.0.0 --port "$PORT" > "$LOG_FILE" 2>&1 &
echo $! > "$PID_FILE"
echo "backend started on port $PORT"
