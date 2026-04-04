# Text Classification Pipeline

The homework notebook implements a classical NLP pipeline for binary sentiment classification on SST-2. This architecture intentionally avoids transformer abstractions and exposes the mechanics of preprocessing, feature construction, and SGD-based optimization.

## Key idea

The pipeline converts raw text into fixed-size bag-of-words vectors, then feeds those vectors into a manually defined logistic regression model in PyTorch.

## Diagram

```mermaid
flowchart TD
    A[SST-2 Dataset] --> B[clean_text]
    B --> C[tokenize]
    C --> D[build_vocabulary top_k=10000]
    D --> E[convert_text_to_vec]
    E --> F[dataset_to_vec]
    F --> G[X_train X_val]
    A --> H[y_train y_val]
    G --> I[LogisticRegression nn.Module]
    H --> J[Binary Targets]
    I --> K[Sigmoid Probabilities]
    J --> L[binary_cross_entropy_loss]
    K --> L
    L --> M[torch.optim.SGD]
    M --> N[Updated Weights and Bias]
    N --> O[Accuracy F1 Sparsity Analysis]
```

## Where it appears

- `clean_text` normalizes raw text
- `tokenize`, `build_vocabulary`, `convert_text_to_vec`, and `dataset_to_vec` construct fixed-length numeric features
- `LogisticRegression` defines the linear classifier
- `sgd_logistic_regression` manages batching, loss computation, regularization, optimization, and metric logging

## Relevant files

- [`../../src/hw1_optimization_pytorch_polished.ipynb`](../../src/hw1_optimization_pytorch_polished.ipynb)
- [`../../src/LLM_Architectures,_hometask_1.ipynb`](../../src/LLM_Architectures,_hometask_1.ipynb)

## Architectural significance

- the pipeline makes feature engineering explicit
- model internals remain inspectable because weights are directly exposed
- L1 regularization is easy to reason about because the representation is sparse and linear
