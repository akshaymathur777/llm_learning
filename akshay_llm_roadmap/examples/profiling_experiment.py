import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.models as models
from torch.profiler import profile, record_function, ProfilerActivity
import os

def run_resnet_profiling():
    print("Setting up ResNet18 experiment...")
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    # 1. Define Model
    model = models.resnet18().to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)
    model.train()

    # 2. Generate Random Data
    # batch size 32, 3 channels, 224x224 images
    inputs = torch.randn(32, 3, 224, 224).to(device)
    labels = torch.randint(0, 1000, (32,)).to(device)

    # Ensure traces directory exists
    os.makedirs("traces", exist_ok=True)

    print("Starting profiling...")
    # 3. Profiling Context Manager
    # Use tensorboard_trace_handler to enable viewing in TensorBoard
    # Results will be saved to ./runs/resnet
    with profile(
        activities=[ProfilerActivity.CPU, ProfilerActivity.CUDA],
        record_shapes=True,
        on_trace_ready=torch.profiler.tensorboard_trace_handler('./runs/resnet')
    ) as prof:
        for i in range(10):  # Run for 10 iterations
            with record_function("model_training_step"):
                optimizer.zero_grad()
                outputs = model(inputs)
                loss = criterion(outputs, labels)
                loss.backward()
                optimizer.step()
                prof.step()  # Need to step the profiler
                print(f"Step {i+1}/10 completed")

    print(f"Profiling complete. Results saved to ./runs/resnet")
    print("Run 'tensorboard --logdir=./runs' to view results.")

if __name__ == "__main__":
    run_resnet_profiling()
