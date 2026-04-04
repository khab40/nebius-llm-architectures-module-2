# Optimization Workflows

The optimization material in this repository moves from intuition to implementation. The Week 2 lecture notebook introduces gradient flow and manual updates, while the homework notebook expands the idea into reusable optimizer routines such as plain gradient descent, momentum, AdaGrad, and Adam.

## Key idea

The architecture separates three concerns:

- define an objective function
- compute gradients through PyTorch autograd
- apply an update rule and record the resulting trajectory

## Diagram

```mermaid
flowchart LR
    A[Objective Function f(theta)] --> B[Initialize Parameters theta0]
    B --> C[Forward Pass]
    C --> D[Compute Loss]
    D --> E[Autograd backward]
    E --> F{Optimizer Rule}
    F --> G[Gradient Descent]
    F --> H[Momentum]
    F --> I[AdaGrad]
    F --> J[Adam]
    G --> K[Update theta]
    H --> K
    I --> K
    J --> K
    K --> L[Zero Gradients]
    L --> M[Store Trajectory and Loss]
    M --> N{More Steps?}
    N -->|Yes| C
    N -->|No| O[Plots and Comparison]
```

## Where it appears

- `run_gd_pytorch` in the Week 2 lecture notebook demonstrates the basic optimization loop
- `gradient_descent`, `momentum`, `adagrad`, and `adam` in the homework notebook provide explicit optimizer implementations for comparison
- plotting helpers render trajectories and objective values to show how update rules behave on easy and difficult surfaces

## Relevant files

- [`../../src/LLM_Architectures,_week_2_Gradient_descent_&_Pytorch.ipynb`](../../src/LLM_Architectures,_week_2_Gradient_descent_&_Pytorch.ipynb)
- [`../../src/hw1_optimization_pytorch_polished.ipynb`](../../src/hw1_optimization_pytorch_polished.ipynb)
- [`../../src/gradient_descent.gif`](../../src/gradient_descent.gif)
- [`../../src/gradient_descent_lr_0.1.gif`](../../src/gradient_descent_lr_0.1.gif)

## Architectural significance

- optimizer behavior is made observable through stored parameter trajectories
- the same computational pattern supports both toy surfaces and real models
- PyTorch autograd is used as the common gradient engine even when update logic is implemented manually
