import os
import time

# Optional imports: torch and wandb may not be installed or configured in the environment.
try:
    import torch
except Exception:
    torch = None

try:
    import wandb
except Exception:
    wandb = None


def main():
    if torch is None:
        print("torch is not installed in this environment. GPU checks will be skipped.")
    else:
        print("torch version:", torch.__version__)
        print("cuda available:", torch.cuda.is_available())
        if torch.cuda.is_available():
            try:
                print("device name:", torch.cuda.get_device_name(0))
            except Exception as e:
                print("error getting device name:", e)

    # Minimal experiment loop — wandb is optional.
    use_wandb = wandb is not None
    if use_wandb:
        # Honor WANDB_MODE env var (offline mode works without an account)
        wandb_mode = os.environ.get("WANDB_MODE", None)
        init_kwargs = {"project": "akshay-llm-roadmap-sandbox", "reinit": True}
        if wandb_mode:
            init_kwargs["mode"] = wandb_mode
        run = wandb.init(**init_kwargs)
    else:
        print("wandb is not installed — proceeding without experiment tracking.")
        run = None

    for i in range(3):
        loss = 1.0 / (i + 1)
        if run is not None:
            wandb.log({"step": i, "loss": loss})
        print(f"step={i}, loss={loss}")
        time.sleep(1)

    if run is not None:
        run.finish()


if __name__ == "__main__":
    main()