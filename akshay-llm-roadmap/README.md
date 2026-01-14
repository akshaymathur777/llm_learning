# akshay-llm-roadmap

Roadmap scaffold for a 6-month AI engineering plan.

Contents:
- setup scripts
- W&B quickstart
- example experiment (wrapper)
- CI and tests

Note on consolidation:
- The canonical implementation of the example is the importable package `akshay_llm_roadmap` (used by tests and CI).
- The `akshay-llm-roadmap/examples/experiment.py` script is a lightweight wrapper that calls the package implementation for convenience.
- To run the example: `python akshay-llm-roadmap/examples/experiment.py`
- To import it in code/tests: `from akshay_llm_roadmap.examples.experiment import run_experiment`
