# akshay-llm-roadmap

Purpose: scaffolding for the 6-month AI Engineering roadmap (planning, tooling, experiments, and onboarding).

## What’s included ✅
- `environment.yml` — conda environment for experiments and dev tools
- `setup.sh` — helper to create the conda env and install recommended packages
- `check_gpu.sh` — quick script to verify `nvidia-smi` and CUDA + PyTorch availability
- `wandb_setup.md` — how to link W&B and a minimal example
- `jira_import.csv` — CSV template for Jira import (sprints / stories / subtasks)
- `.github/ISSUE_TEMPLATE/` — GitHub issue templates: Work / Side / Smol / Learning
- `examples/experiment.py` — minimal example logging to W&B and checking GPU
- `.github/workflows/ci.yml` — basic CI: lint + tests

## Quick start
1. Use a Python virtual environment (venv) or your preferred manager (pyenv/virtualenv/poetry). This repo defaults to a venv + pip workflow.

2. Create and activate the virtual environment:

```bash
# Option A: helper script (recommended)
bash akshay-llm-roadmap/setup.sh
source akshay-llm-roadmap/venv/bin/activate

# Option B: manual
python -m venv venv
source venv/bin/activate
pip install -r akshay-llm-roadmap/requirements.txt
```

> Note: If you prefer conda, `environment.yml` is included as an optional artifact with the same packages; install a CUDA-enabled `torch` build per the official PyTorch instructions when using GPUs.

3. Verify GPU:

```bash
bash akshay-llm-roadmap/check_gpu.sh
python akshay-llm-roadmap/examples/experiment.py
```

## Courses & resources 📚
- Smol‑Course: https://github.com/huggingface/smol-course
- LLM Course: https://huggingface.co/learn/llm-course/chapter1/1
- MCP Course: https://huggingface.co/learn/mcp-course/unit0/introduction
- Agents Course: https://huggingface.co/learn/agents-course/unit0/introduction

---

If you want, I can: create a feature branch, push these files, and open a PR; or create a remote repo (I’ll need a GitHub token and visibility preference).