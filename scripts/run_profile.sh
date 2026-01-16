#!/bin/bash

# LF-3 Profiling Runner
# Usage: ./scripts/run_profile.sh [cnn|llm]

EXPERIMENT_TYPE=$1

if [ -z "$EXPERIMENT_TYPE" ]; then
    echo "Usage: $0 [cnn|llm]"
    exit 1
fi

# Ensure we are in the root directory
cd "$(dirname "$0")/.."

# Activate virtual environment if it exists
if [ -d ".venv" ]; then
    source .venv/bin/activate
fi

# Create logs directory
mkdir -p logs

TIMESTAMP=$(date +%Y%m%d_%H%M%S)
GPU_LOG="logs/gpu_log_${EXPERIMENT_TYPE}_${TIMESTAMP}.csv"

echo "Starting GPU logging to $GPU_LOG..."
# Start nvidia-smi in background
# Loop every 1 second
nvidia-smi --query-gpu=timestamp,utilization.gpu,utilization.memory,memory.total,memory.free,memory.used --format=csv --loop=1 --filename="$GPU_LOG" &
NVIDIA_PID=$!

echo "Running $EXPERIMENT_TYPE experiment..."
if [ "$EXPERIMENT_TYPE" == "cnn" ]; then
    python3 akshay_llm_roadmap/examples/profiling_experiment.py
elif [ "$EXPERIMENT_TYPE" == "llm" ]; then
    python3 akshay_llm_roadmap/examples/profiling_llm.py
else
    echo "Unknown experiment type: $EXPERIMENT_TYPE"
    kill $NVIDIA_PID
    exit 1
fi

echo "Experiment finished. Stopping GPU logging..."
kill $NVIDIA_PID

echo "Done. Check traces/ and logs/ for output."
