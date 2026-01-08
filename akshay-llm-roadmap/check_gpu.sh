#!/usr/bin/env bash
set -euo pipefail

echo "=== nvidia-smi output ==="
if command -v nvidia-smi >/dev/null 2>&1; then
  nvidia-smi
else
  echo "nvidia-smi not found. You might not have NVIDIA drivers installed or are on a CPU-only machine."
fi

echo "\n=== Python / torch GPU check ==="
python - <<'PY'
import torch
print('torch version:', torch.__version__)
print('cuda available:', torch.cuda.is_available())
if torch.cuda.is_available():
    print('cuda device count:', torch.cuda.device_count())
    try:
        print('device name:', torch.cuda.get_device_name(0))
    except Exception as e:
        print('error getting device name:', e)
PY