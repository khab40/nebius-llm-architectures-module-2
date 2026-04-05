# Experimentation and Evaluation

The repository is designed not just to train models, but to compare decisions across the [Nebius AI Performance Engineering](https://academy.nebius.com/ai-engineering-uk) learning exercises. The notebooks repeatedly follow the same architecture: configure a model or optimizer, train it, evaluate it with metrics, and visualize the outcome for interpretation.

## Key idea

Experimentation is treated as a reusable loop with configurable knobs rather than a one-off script.

## Diagram

```mermaid
flowchart TD
    A[Choose Task and Dataset] --> B[Configure Hyperparameters]
    B --> C[Train Model]
    C --> D[Collect History]
    D --> E[Evaluate Metrics]
    E --> F[Generate Tables and Plots]
    F --> G[Compare Runs]
    G --> H[Write Conclusions]

    C --> I[Weights Biases Trajectories]
    C --> J[Loss Curves]
    E --> K[Accuracy]
    E --> L[F1]
    E --> M[ROC AUC]
    E --> N[Confusion Matrix]
```

## Where it appears

- the homework notebook sweeps learning rate, batch size, initialization, and regularization settings
- the report notebook condenses selected experiments into a presentation-friendly summary
- the Week 2 notebook evaluates a tabular weather classification pipeline with standard metrics and preprocessing

## Relevant files

- [`../../src/hw1_optimization_pytorch_polished.ipynb`](../../src/hw1_optimization_pytorch_polished.ipynb)
- [`../../src/pytorch_optimization_report.ipynb`](../../src/pytorch_optimization_report.ipynb)
- [`../../src/LLM_Architectures,_week_2_Gradient_descent_&_Pytorch.ipynb`](../../src/LLM_Architectures,_week_2_Gradient_descent_&_Pytorch.ipynb)
- [`../../src/weatherAUS.csv`](../../src/weatherAUS.csv)

## Architectural significance

- experiments are structured to make tradeoffs visible rather than hidden
- metrics and plots are part of the architecture, not an afterthought
- the same evaluation pattern supports both tabular classification and text classification studies
