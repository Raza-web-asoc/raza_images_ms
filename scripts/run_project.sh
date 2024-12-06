#!/usr/bin/env bash

set -a
source .env
set +a


PORT="${PORT:-8000}"

uvicorn app.src.main:app  --host 0.0.0.0 --port 8000 --reload