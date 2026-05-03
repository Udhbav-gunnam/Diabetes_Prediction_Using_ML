#!/bin/bash
cd "$(dirname "$0")"

BACKEND_DIR="./backend"
FRONTEND_DIR="./frontend"
BACKEND_PORT=5000
FRONTEND_PORT=8080

cd "$BACKEND_DIR" || exit
nohup python app.py > flask.log 2>&1 &
BACKEND_PID=$!
cd ..

cd "$FRONTEND_DIR" || exit
nohup python3 -m http.server "$FRONTEND_PORT" > frontend.log 2>&1 &
FRONTEND_PID=$!
cd ..

sleep 2
xdg-open "http://localhost:$FRONTEND_PORT/index.html"

read

kill "$BACKEND_PID"
kill "$FRONTEND_PID"

