# akshay-llm-roadmap

Roadmap scaffold for a 6-month AI engineering plan.

Contents:
- setup scripts
- W&B quickstart
- example experiment (package)
- CI and tests

Note on consolidation:
- The canonical implementation of the example is the importable package `akshay_llm_roadmap` (used by tests and CI).
- To import it in code/tests: `from akshay_llm_roadmap.examples.experiment import run_experiment`
- To run the example directly: `python -c "from akshay_llm_roadmap.examples.experiment import run_experiment; print(run_experiment())"`
