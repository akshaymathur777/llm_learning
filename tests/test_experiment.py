from akshay_llm_roadmap.examples.experiment import run_experiment


def test_run_experiment_basic():
    result = run_experiment(log_to_wandb=False)
    assert isinstance(result, dict)
    assert "metric" in result
    assert result["metric"] == 0.42
