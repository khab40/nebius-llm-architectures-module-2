# LLM Architectures Module 2

This repository contains study material, experiments, and homework artifacts for Module 2 of the [Nebius AI Performance Engineering](https://academy.nebius.com/ai-engineering-uk) course. The focus of this module is optimization fundamentals for modern ML systems: gradient flow, gradient descent, stochastic optimization, PyTorch autodiff, classical feature pipelines, and practical model training for classification tasks.

The project is notebook-first. Most of the implementation lives in Jupyter notebooks and is organized around learning flows, experiments, and polished homework deliverables rather than a conventional Python package layout.

## Scope

Module 2 covers four connected themes:

- gradient flow and gradient descent intuition on simple functions
- PyTorch autograd and parameter updates
- structured preprocessing and model training for classification tasks
- optimization behavior under different objectives, regularization choices, and optimizers

## Main Artifacts

### Core notebooks

- [`src/LLM_Architectures,_week_2_Gradient_descent_&_Pytorch.ipynb`](src/LLM_Architectures,_week_2_Gradient_descent_&_Pytorch.ipynb): lecture and lab notebook for gradient flow, manual gradient descent, PyTorch autodiff, SGD for linear regression, weather classification, and softmax stability discussion
- [`src/hw1_optimization_pytorch_polished.ipynb`](src/hw1_optimization_pytorch_polished.ipynb): polished homework notebook covering SST-2 preprocessing, Bag-of-Words vectorization, logistic regression in PyTorch, SGD training, L1 regularization, and optimizer comparisons
- [`src/pytorch_optimization_report.ipynb`](src/pytorch_optimization_report.ipynb): compact report notebook summarizing selected optimization experiments and visual outputs
- [`src/Week_6_practice_session.ipynb`](src/Week_6_practice_session.ipynb): additional PyTorch training practice focused on neural network construction and gradient descent workflows

### Supporting assets

- [`src/LLM_Architectures,_hometask_1.ipynb`](src/LLM_Architectures,_hometask_1.ipynb): homework copy aligned with the polished optimization assignment
- [`src/weatherAUS.csv`](src/weatherAUS.csv): tabular dataset used in the classification section of the Week 2 notebook
- [`src/gradient_descent.gif`](src/gradient_descent.gif): optimization visualization asset
- [`src/gradient_descent_lr_0.1.gif`](src/gradient_descent_lr_0.1.gif): optimization visualization asset for a specific learning rate
- [`src/notebook_theme.css`](src/notebook_theme.css): shared Nebius Academy-inspired presentation layer applied across notebooks

### Minimal Python package

- [`src/workspace/__main__.py`](src/workspace/__main__.py): small entry point for workspace validation
- [`tests/test_workspace.py`](tests/test_workspace.py): sanity test for the package entry point
- [`pyproject.toml`](pyproject.toml): project metadata and test configuration
- [`requirements.txt`](requirements.txt): notebook and experimentation dependencies

## Architecture Documentation

Project architecture notes are documented separately under [`docs/architecture`](docs/architecture):

- [`docs/architecture/01-module-overview.md`](docs/architecture/01-module-overview.md): repository-level learning architecture and artifact relationships
- [`docs/architecture/02-optimization-workflows.md`](docs/architecture/02-optimization-workflows.md): gradient descent, momentum, AdaGrad, and Adam execution flow
- [`docs/architecture/03-text-classification-pipeline.md`](docs/architecture/03-text-classification-pipeline.md): SST-2 preprocessing, vocabulary building, vectorization, and logistic regression training pipeline
- [`docs/architecture/04-experimentation-and-evaluation.md`](docs/architecture/04-experimentation-and-evaluation.md): experiment loops, metrics, comparisons, and reporting outputs
- [`docs/architecture/05-notebook-presentation-layer.md`](docs/architecture/05-notebook-presentation-layer.md): notebook theming and shared presentation strategy

## Repository Layout

```text
.
├── docs/
│   └── architecture/
├── src/
│   ├── *.ipynb
│   ├── notebook_theme.css
│   ├── weatherAUS.csv
│   └── workspace/
├── tests/
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Working Model

The repository is designed for interactive exploration:

1. open the relevant notebook for the topic you want to study
2. execute cells sequentially to reproduce the experiments
3. compare optimizer behavior, model metrics, and visualization outputs
4. use the report notebook to consolidate results into a concise summary

The notebooks share a common visual layer through [`src/notebook_theme.css`](src/notebook_theme.css), which keeps styling consistent while avoiding large inline CSS blobs inside each `.ipynb`.

## Environment

Typical local setup:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .[dev]
pytest
python -m workspace
```

## Notes

- This repository is primarily an educational workspace, not a production application.
- The main implementation logic is embedded in notebooks, so architectural boundaries are conceptual rather than package-enforced.
- The most representative notebooks for Module 2 are the Week 2 lecture notebook and the polished optimization homework notebook.
