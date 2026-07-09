#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PID_FILE="$ROOT_DIR/backend.pid"

if [[ ! -f "$PID_FILE" ]]; then
  echo "pid file not found"
  exit 0
fi

PID="$(cat "$PID_FILE")"
if [[ -n "${PID}" ]] && kill -0 "$PID" 2>/dev/null; then
  kill "$PID"
  echo "backend stopped"
else
  echo "process not running"
fi

rm -f "$PID_FILE"
