# Weights & Biases (W&B) quick setup

1. Create an account at https://wandb.ai/ and get your API key from Settings → API Keys.
2. Locally: `pip install wandb` (already included in `environment.yml`).
3. Login:

```bash
# Option A: interactive
wandb login

# Option B: use env var (CI-friendly)
export WANDB_API_KEY="<your_key_here>"
```

4. Minimal use in code:

```py
import wandb
wandb.init(project="akshay-llm-roadmap-sandbox", entity="<your-entity>")
wandb.log({"loss": 0.1})
```

5. Link W&B project to your repo and team via the W&B UI. For CI, store `WANDB_API_KEY` as a secret and use it in workflows.

Troubleshooting tips:
- If runs fail to appear, confirm `WANDB_API_KEY` is set and `wandb.init()` succeeded.
- For large logs (models/artifacts), use `wandb.save()`/`wandb.Artifact` patterns.