#!/bin/bash

# Configuration Variables
PORT=4723
HOST="127.0.0.1"
LOG_FILE="artifacts/appium-logs/appium.log"
TIMEOUT=30

mkdir -p "artifacts/appium-logs"

echo "Checking if port $PORT is already in use..."
if lsof -i :$PORT > /dev/null ; then
    echo "⚠️ Port $PORT is already in use! Killing the existing process..."
    kill -9 $(lsof -t -i:$PORT)
    sleep 2
fi

echo "🚀 Starting Appium Server on $HOST:$PORT..."
# Start Appium in the background and redirect output to a log file
appium --address $HOST --port $PORT --allow-cors > $LOG_FILE 2>&1 &
APPIUM_PID=$!

echo "⏳ Waiting for Appium server to respond..."
COUNTER=0
while ! curl -s http://$HOST:$PORT/status > /dev/null; do
    sleep 1
    COUNTER=$((COUNTER + 1))
    
    if [ $COUNTER -ge $TIMEOUT ]; then
        echo "❌ Error: Appium server failed to start within $TIMEOUT seconds."
        echo "=== APPIUM LOG OUTPUT ==="
        cat $LOG_FILE
        exit 1
    fi
done

echo "✅ Appium Server is successfully up and running (PID: $APPIUM_PID)!"

