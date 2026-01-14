"""Minimal experiment that optionally logs to wandb (package path).
"""

def run_experiment(log_to_wandb=False):
    result = {"metric": 0.42}
    if log_to_wandb:
        try:
            import wandb
            wandb.init(project="llm-roadmap-example", mode="disabled")
            wandb.log(result)
            wandb.finish()
        except Exception:
            pass
    return result


if __name__ == "__main__":
    print(run_experiment(log_to_wandb=False))
