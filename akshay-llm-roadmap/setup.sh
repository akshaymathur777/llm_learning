#!/usr/bin/env bash
set -euo pipefail

ENV_DIR="venv"
THIS_DIR="$(cd "$(dirname "$0")" && pwd)"
PYTHON_CMD="$(command -v python3 || command -v python || true)"

if [ -z "$PYTHON_CMD" ]; then
  echo "No python executable found (python3 or python). Please install Python 3.10+."
  exit 1
fi

echo "Creating virtualenv at '${THIS_DIR}/${ENV_DIR}' using ${PYTHON_CMD}"
$PYTHON_CMD -m venv "${THIS_DIR}/${ENV_DIR}"

echo "Activating venv and upgrading pip"
# shellcheck disable=SC1091
source "${THIS_DIR}/${ENV_DIR}/bin/activate"
python -m pip install --upgrade pip

if [ "${FULL_INSTALL:-0}" = "1" ]; then
  if [ -f "${THIS_DIR}/requirements.txt" ]; then
    pip install -r "${THIS_DIR}/requirements.txt"
  else
    echo "requirements.txt not found, installing core packages..."
    pip install torch transformers deepspeed wandb accelerate datasets
  fi
else
  echo "Installing minimal development dependencies (wandb, pytest, flake8)."
  pip install wandb pytest flake8
  echo "To install full stack (torch, deepspeed, etc.) set FULL_INSTALL=1 and re-run this script."
fi

echo "To activate: source ${THIS_DIR}/${ENV_DIR}/bin/activate"
echo "If you have a CUDA-capable GPU, follow the official PyTorch instructions to install a CUDA build of torch."
echo "Optional: install Deepspeed GPU dependencies (see Deepspeed docs)"