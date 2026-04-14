# Nebius AI Performance Engineering Notebook Workspace

This repository is a notebook-first workspace for the Nebius AI Performance Engineering course. It contains completed homework submissions, experiment notebooks, supporting visual assets, and a tiny Python package used only for a sanity check.

Most implementation work lives in Jupyter notebooks under `src/`. The notebooks cover optimization fundamentals, PyTorch training loops, CIFAR-10 classification, character-level RNN language modeling, and from-scratch NumPy neural-network layers.

## Current Contents

### Core Homework Notebooks

- [`src/hw1/HW_1_sub.ipynb`](src/hw1/HW_1_sub.ipynb): earlier homework submission covering text-classification and optimization tasks.
- [`src/hw2/HW2_Gradient_descent_&_Pytorch.ipynb`](src/hw2/HW2_Gradient_descent_&_Pytorch.ipynb): gradient descent, PyTorch autograd, optimizer behavior, weather classification, and softmax stability work.
- [`src/hw4/HW4_p1_CIFAR10_sub.ipynb`](src/hw4/HW4_p1_CIFAR10_sub.ipynb): CIFAR-10 submission notebook with custom dataset handling, binary classification, multi-class classification, and links to the separate experiment notebooks.
- [`src/hw4/HW4_p2_RNN_LM_sub.ipynb`](src/hw4/HW4_p2_RNN_LM_sub.ipynb): character-level dinosaur-name language model with one-hot encoding, LSTM training, top-k and temperature sampling, beam search, Apple Silicon device setup, and conclusions from executed results.

### Week 4 Experiment Notebooks

- [`src/hw4/HW4_p1_task_1_4_exp.ipynb`](src/hw4/HW4_p1_task_1_4_exp.ipynb): CIFAR-10 Task 1.4 experiment notebook with plots and conclusions.
- [`src/hw4/HW4_p1_task_1_5_cat_dog_exp.ipynb`](src/hw4/HW4_p1_task_1_5_cat_dog_exp.ipynb): CIFAR-10 Task 1.5 cat-vs-dog experiment notebook with plots and conclusions.
- [`src/hw4/HW4_p1_task_3_exp.ipynb`](src/hw4/HW4_p1_task_3_exp.ipynb): CIFAR-10 Task 3 experiment notebook comparing MLP and CNN runs, including Apple Silicon setup, training plots, exact achieved metrics, and conclusions.

### Week 4 Bonus Notebooks

- [`src/hw4/HW4_bon_p2_forward_sub.ipynb`](src/hw4/HW4_bon_p2_forward_sub.ipynb): from-scratch NumPy forward-pass notebook implementing `Module`, `Linear`, `Sigmoid`, and `NN`, with a smoke experiment, sigmoid plot, Apple Silicon availability check, and conclusions.
- [`src/hw4/HW4_bon_p1_backward_sub.ipynb`](src/hw4/HW4_bon_p1_backward_sub.ipynb): from-scratch NumPy backward-pass notebook implementing linear/sigmoid gradients, network backpropagation, log loss, full-batch training, mini-batch SGD, image-classification smoke testing, plots, and conclusions from executed results.

### Practice, Reports, Assets, and Data

- [`src/hw2/pytorch_optimization_report.ipynb`](src/hw2/pytorch_optimization_report.ipynb): compact optimization report notebook.
- [`src/hw2/bonus_rosenbrock_optimizers.ipynb`](src/hw2/bonus_rosenbrock_optimizers.ipynb): additional Rosenbrock optimizer exploration.
- [`src/Week_6_practice_session.ipynb`](src/Week_6_practice_session.ipynb): additional PyTorch training practice.
- [`src/hw4/RNN_demo.ipynb`](src/hw4/RNN_demo.ipynb): RNN demonstration notebook.
- [`src/basics-test.ipynb`](src/basics-test.ipynb): small local notebook checks and exploratory experiments.
- [`docs/LLM_Optimization_Tutorial_v3.pdf`](docs/LLM_Optimization_Tutorial_v3.pdf): supporting optimization tutorial material.
- [`docs/gradient_descent.gif`](docs/gradient_descent.gif), [`docs/gradient_descent_lr_0.1.gif`](docs/gradient_descent_lr_0.1.gif), and [`docs/rosenbrock_shared_compass_fixed_1.gif`](docs/rosenbrock_shared_compass_fixed_1.gif): optimization visualization assets.
- [`src/notebook_theme.css`](src/notebook_theme.css): shared notebook presentation styling.

Local downloaded datasets and runtime artifacts should stay out of git unless intentionally promoted to source artifacts. Homework notebooks use `src/data/` from their grouped `src/hw*/` folders, and that directory is ignored.

## Architecture Notes

Repository-level notes live under [`docs/architecture`](docs/architecture):

- [`docs/architecture/01-module-overview.md`](docs/architecture/01-module-overview.md): repository-level learning architecture and artifact relationships.
- [`docs/architecture/02-optimization-workflows.md`](docs/architecture/02-optimization-workflows.md): gradient descent, momentum, AdaGrad, and Adam execution flow.
- [`docs/architecture/03-text-classification-pipeline.md`](docs/architecture/03-text-classification-pipeline.md): SST-2 preprocessing, vocabulary building, vectorization, and logistic regression training pipeline.
- [`docs/architecture/04-experimentation-and-evaluation.md`](docs/architecture/04-experimentation-and-evaluation.md): experiment loops, metrics, comparisons, and reporting outputs.
- [`docs/architecture/05-notebook-presentation-layer.md`](docs/architecture/05-notebook-presentation-layer.md): notebook theming and shared presentation strategy.
- [`docs/architecture/06-cifar10-submission-flow.md`](docs/architecture/06-cifar10-submission-flow.md): Week 4 CIFAR-10 binary and multi-class classification task flow.
- [`docs/architecture/07-rnn-lm-submission-flow.md`](docs/architecture/07-rnn-lm-submission-flow.md): Week 4 character-level RNN language-modeling task flow.
- [`docs/architecture/08-forward-pass-submission-flow.md`](docs/architecture/08-forward-pass-submission-flow.md): Week 4 forward-pass bonus task flow.
- [`docs/architecture/09-backward-pass-submission-flow.md`](docs/architecture/09-backward-pass-submission-flow.md): Week 4 backward-pass bonus task flow.

HW4-focused architecture notes live in the main architecture folder:

- [`docs/architecture/01-cifar10-classification.md`](docs/architecture/01-cifar10-classification.md): architecture for the CIFAR-10 submission notebook and Task 1.4, 1.5, and 3 experiment notebooks.
- [`docs/architecture/02-rnn-language-modeling.md`](docs/architecture/02-rnn-language-modeling.md): architecture for the dinosaur-name RNN language model and companion RNN demo.
- [`docs/architecture/03-forward-pass-framework.md`](docs/architecture/03-forward-pass-framework.md): architecture for the NumPy forward-pass bonus framework.
- [`docs/architecture/04-backward-pass-framework.md`](docs/architecture/04-backward-pass-framework.md): architecture for the NumPy backward-pass bonus framework.

## Minimal Python Package

The repository also contains a minimal package and test used to verify that the workspace is importable:

- [`src/workspace/__main__.py`](src/workspace/__main__.py): prints a simple workspace readiness message.
- [`tests/test_workspace.py`](tests/test_workspace.py): sanity test for the package entry point.
- [`pyproject.toml`](pyproject.toml): project metadata and pytest configuration.
- [`uv.lock`](uv.lock): locked dependency resolution generated by uv.

## Repository Layout

```text
.
├── docs/
│   └── architecture/
├── src/
│   ├── hw1/
│   ├── hw2/
│   ├── hw4/
│   ├── Week_6_practice_session.ipynb
│   ├── basics-test.ipynb
│   ├── data/
│   ├── notebook_theme.css
│   └── workspace/
├── tests/
├── CHANGELOG.md
├── pyproject.toml
├── uv.lock
└── README.md
```

## Environment

Typical local setup:

```bash
uv sync --group dev
uv run pytest
uv run python -m workspace
```

To start Jupyter from the managed uv environment:

```bash
uv run jupyter lab
```

## Working Model

Use this repository as an interactive notebook workspace:

1. Open the relevant notebook under `src/hw1/`, `src/hw2/`, or `src/hw4/`.
2. Execute cells sequentially to reproduce setup, training, plots, and conclusions.
3. Use the separate experiment notebooks for longer CIFAR-10 runs and comparisons.
4. Keep downloaded datasets and generated runtime files out of git unless they are intentionally promoted to source artifacts.

## Notes

- The original `*_orig.ipynb` notebooks were removed; the tracked notebooks now focus on completed submission and experiment artifacts.
- Some notebooks include executed outputs and conclusions based on those outputs.
- Apple Silicon checks are included where they are relevant, but the from-scratch NumPy notebooks still run their model computations on CPU.
