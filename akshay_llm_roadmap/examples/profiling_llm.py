import torch
import torch.nn as nn
import torch.optim as optim
from transformers import GPT2Config, GPT2LMHeadModel
from torch.profiler import profile, record_function, ProfilerActivity
import os

def run_llm_profiling():
    print("Setting up GPT-2 experiment...")
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    # 1. Define Model (Small GPT-2)
    # Using a smaller config for faster profiling demonstration
    config = GPT2Config(
        n_layer=4,
        n_head=4,
        n_embd=256,
        vocab_size=1000  # Small vocab for demo
    )
    model = GPT2LMHeadModel(config).to(device)
    model.train()
    
    optimizer = optim.AdamW(model.parameters(), lr=1e-4)

    # 2. Generate Random Data
    # batch size 8, sequence length 32
    input_ids = torch.randint(0, 1000, (8, 32)).to(device)
    labels = input_ids.clone()

    # Ensure traces directory exists
    os.makedirs("traces", exist_ok=True)

    print("Starting profiling...")
    # 3. Profiling Context Manager
    # Use tensorboard_trace_handler to enable viewing in TensorBoard
    # Results will be saved to ./runs/llm
    with profile(
        activities=[ProfilerActivity.CPU, ProfilerActivity.CUDA],
        record_shapes=True,
        on_trace_ready=torch.profiler.tensorboard_trace_handler('./runs/llm')
    ) as prof:
        for i in range(10):  # Run for 10 iterations
            with record_function("model_training_step"):
                optimizer.zero_grad()
                outputs = model(input_ids, labels=labels)
                loss = outputs.loss
                loss.backward()
                optimizer.step()
                prof.step()
                print(f"Step {i+1}/10 completed")

    print(f"Profiling complete. Results saved to ./runs/llm")
    print("Run 'tensorboard --logdir=./runs' to view results.")

if __name__ == "__main__":
    run_llm_profiling()
