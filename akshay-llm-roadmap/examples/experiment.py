"""Minimal experiment that optionally logs to wandb.
Designed to be importable and testable without heavy deps.
"""

def run_experiment(log_to_wandb=False):
    """Run a trivial experiment and optionally log to wandb.

    Returns a dict with a single metric so tests can assert on it.
    """
    result = {"metric": 0.42}
    if log_to_wandb:
        try:
            import wandb
            wandb.init(project="llm-roadmap-example", mode="disabled")
            wandb.log(result)
            wandb.finish()
        except Exception:
            # If wandb not installed or fails, proceed silently (tests don't require it)
            pass
    return result


if __name__ == "__main__":
    print(run_experiment(log_to_wandb=False))
