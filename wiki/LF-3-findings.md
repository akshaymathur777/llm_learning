# LF-3 Profiling Findings

## Overview
We implemented infrastructure to profile PyTorch training runs for both CNN (ResNet18) and LLM (GPT-2) models.

## How to Run
Use the `run_profile.sh` script to run experiments and capture GPU utilization.

```bash
# For CNN
./scripts/run_profile.sh cnn

# For LLM
./scripts/run_profile.sh llm
```

## Outputs
- **Traces**: Saved in `traces/` as JSON files (e.g., `trace_resnet.json`, `trace_llm.json`).
  - **View**: Open **[https://ui.perfetto.dev/](https://ui.perfetto.dev/)** and drag-and-drop the JSON file. `chrome://tracing` is deprecated.
- **logs**: GPU utilization logs saved in `logs/` as CSV files.

## Detailed Findings by Model

### 1. CNN (ResNet18)
- **Observed Behavior**:
  - **GPU Utilization**: Low (~13%).
  - **Memory Usage**: Low (~6% of 16GB).
  - **Bottleneck**: **CPU / Data Loading**.
- **Analysis**:
  - The model is small (`resnet18`), so the GPU computes gradients very quickly.
  - The CPU (Python) generates random data one batch at a time in the main process.
  - **Trace Expectation**: If you look at the trace, you will likely see large gaps between GPU kernels where the CPU is preparing the next batch.
- **Learning Point**: To fix this in a real training run, you would use `DataLoader` with multiple workers to pre-fetch data in parallel.

### 2. LLM (GPT-2)
- **Observed Behavior**:
  - **GPU Utilization**: Extremely low (~3%).
  - **Memory Usage**: Low (~4%).
  - **Bottleneck**: **Kernel Launch Overhead / Python Overhead**.
- **Analysis**:
  - We used a custom *tiny* config (`n_layer=4`, `n_embd=256`) and a batch size of 8.
  - The GPU spends more time *launching* the kernels than actually *executing* them.
  - The "Arithmetic Intensity" (compute per byte of memory) is too low for the GPU to shine.
- **Learning Point**: LLMs need massive batch sizes (tokens) to saturate modern GPUs. You would typically increase the batch size until you run out of memory.

## Recommendations for Next Experiments
1. **Saturate the GPU**: Increase batch size for ResNet to 128 or 256.
2. **Real Data Pipeline**: Replace random tensor generation with a `DataLoader` wrapping `FakeData` or a real dataset like CIFAR-10.
3. **Larger LLM**: Try loading `gpt2-medium` or `bert-base-cased` to see higher memory usage and compute load.

