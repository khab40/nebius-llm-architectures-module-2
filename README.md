# Nebius AI Performance Engineering Notebook Workspace

This repository contains notebook-first study material, experiments, and homework artifacts for the Nebius AI Performance Engineering course. The work is centered on optimization fundamentals, PyTorch training loops, image classification, recurrent language modeling, and from-scratch neural-network mechanics.

The project is not a conventional production package. Most of the implementation lives in Jupyter notebooks under `src/`, with a small Python package used only as a workspace sanity check.

## Scope

The current source tree covers these learning areas:

- gradient descent, optimizer behavior, PyTorch autograd, and optimization visualizations
- tabular and text classification pipelines from earlier homework
- CIFAR-10 binary and multi-class image classification with flattened images and PyTorch networks
- character-level RNN language modeling with an LSTM over dinosaur-name sequences
- from-scratch NumPy implementations of fully connected layers, sigmoid activations, forward propagation, backward propagation, log loss, and stochastic mini-batch training

## Main Artifacts

### Optimization and Earlier Homework

- [`src/LLM_Architectures,_week_2_Gradient_descent_&_Pytorch.ipynb`](src/LLM_Architectures,_week_2_Gradient_descent_&_Pytorch.ipynb): lecture and lab notebook for gradient flow, manual gradient descent, PyTorch autodiff, SGD for linear regression, weather classification, and softmax stability discussion
- [`src/LLM_Architectures_hometask_1_original.ipynb`](src/LLM_Architectures_hometask_1_original.ipynb): original homework notebook for the earlier text classification and optimization assignment
- [`src/LLM_Architectures_hometask_1_submission.ipynb`](src/LLM_Architectures_hometask_1_submission.ipynb): submission notebook covering SST-2 preprocessing, Bag-of-Words vectorization, logistic regression in PyTorch, optimizer comparisons, regularization, and Rosenbrock experiments
- [`src/pytorch_optimization_report.ipynb`](src/pytorch_optimization_report.ipynb): compact report notebook summarizing selected optimization experiments and visual outputs
- [`src/bonus_rosenbrock_optimizers.ipynb`](src/bonus_rosenbrock_optimizers.ipynb): additional Rosenbrock optimizer exploration

### Week 4 Neural-Network Homework

- [`src/LLM_Architectures_W4_p1_homework_CIFAR10_original.ipynb`](src/LLM_Architectures_W4_p1_homework_CIFAR10_original.ipynb): original CIFAR-10 image-classification task notebook
- [`src/LLM_Architectures_W4_p1_homework_CIFAR10_submission.ipynb`](src/LLM_Architectures_W4_p1_homework_CIFAR10_submission.ipynb): working submission notebook for flattened CIFAR-10 binary classification, a custom `Dataset`, and multi-class classification
- [`src/LLM_Architectures_W4_p2_homework_RNN_LM_original.ipynb`](src/LLM_Architectures_W4_p2_homework_RNN_LM_original.ipynb): original character-level language-modeling task notebook
- [`src/LLM_Architectures_W4_p2_homework_RNN_LM_submission.ipynb`](src/LLM_Architectures_W4_p2_homework_RNN_LM_submission.ipynb): working submission notebook for a dinosaur-name character RNN, one-hot encoding, LSTM training, sampling, top-k sampling, temperature sampling, and beam-search extension work
- [`src/LLM_Architectures_W4_homework_bonus_p2_forward_original.ipynb`](src/LLM_Architectures_W4_homework_bonus_p2_forward_original.ipynb): original from-scratch forward-pass bonus task
- [`src/LLM_Architectures_W4_homework_bonus_p2_forward_submission.ipynb`](src/LLM_Architectures_W4_homework_bonus_p2_forward_submission.ipynb): working submission notebook for NumPy `Module`, `Linear`, `Sigmoid`, and `NN` forward propagation
- [`src/LLM_Architectures_W4_homework_bonus_p1_backward_original.ipynb`](src/LLM_Architectures_W4_homework_bonus_p1_backward_original.ipynb): original from-scratch backward-pass bonus task
- [`src/LLM_Architectures_W4_homework_bonus_p1_backward_submission.ipynb`](src/LLM_Architectures_W4_homework_bonus_p1_backward_submission.ipynb): working submission notebook for manual gradients, backward propagation, log loss, batch training, stochastic mini-batch training, and MNIST 0-vs-1 testing

### Practice, Assets, and Data

- [`src/Week_6_practice_session.ipynb`](src/Week_6_practice_session.ipynb): additional PyTorch training practice focused on neural network construction and gradient descent workflows
- [`src/RNN_demo.ipynb`](src/RNN_demo.ipynb): RNN demonstration notebook
- [`src/basics-test.ipynb`](src/basics-test.ipynb): small exploratory notebook for local notebook checks and simple experiments
- [`src/weatherAUS.csv`](src/weatherAUS.csv): tabular dataset used in the classification section of the Week 2 notebook
- `src/data/`: local ignored cache for downloaded CIFAR-10 data
- [`src/LLM_Optimization_Tutorial_v3.pdf`](src/LLM_Optimization_Tutorial_v3.pdf): supporting optimization tutorial material
- [`src/gradient_descent.gif`](src/gradient_descent.gif), [`src/gradient_descent_lr_0.1.gif`](src/gradient_descent_lr_0.1.gif), and [`src/rosenbrock_shared_compass_fixed_1.gif`](src/rosenbrock_shared_compass_fixed_1.gif): optimization visualization assets
- [`src/notebook_theme.css`](src/notebook_theme.css): shared notebook presentation styling

### Minimal Python Package

- [`src/workspace/__main__.py`](src/workspace/__main__.py): small entry point for workspace validation
- [`tests/test_workspace.py`](tests/test_workspace.py): sanity test for the package entry point
- [`pyproject.toml`](pyproject.toml): project metadata and test configuration
- [`requirements.txt`](requirements.txt): notebook and experimentation dependencies

## Architecture Documentation

Project architecture notes are documented under [`docs/architecture`](docs/architecture):

- [`docs/architecture/01-module-overview.md`](docs/architecture/01-module-overview.md): repository-level learning architecture and artifact relationships
- [`docs/architecture/02-optimization-workflows.md`](docs/architecture/02-optimization-workflows.md): gradient descent, momentum, AdaGrad, and Adam execution flow
- [`docs/architecture/03-text-classification-pipeline.md`](docs/architecture/03-text-classification-pipeline.md): SST-2 preprocessing, vocabulary building, vectorization, and logistic regression training pipeline
- [`docs/architecture/04-experimentation-and-evaluation.md`](docs/architecture/04-experimentation-and-evaluation.md): experiment loops, metrics, comparisons, and reporting outputs
- [`docs/architecture/05-notebook-presentation-layer.md`](docs/architecture/05-notebook-presentation-layer.md): notebook theming and shared presentation strategy
- [`docs/architecture/06-cifar10-submission-flow.md`](docs/architecture/06-cifar10-submission-flow.md): Week 4 CIFAR-10 binary and multi-class classification task flow
- [`docs/architecture/07-rnn-lm-submission-flow.md`](docs/architecture/07-rnn-lm-submission-flow.md): Week 4 character-level RNN language-modeling task flow
- [`docs/architecture/08-forward-pass-submission-flow.md`](docs/architecture/08-forward-pass-submission-flow.md): Week 4 forward-pass bonus task flow
- [`docs/architecture/09-backward-pass-submission-flow.md`](docs/architecture/09-backward-pass-submission-flow.md): Week 4 backward-pass bonus task flow

## Repository Layout

```text
.
├── docs/
│   └── architecture/
├── src/
│   ├── *.ipynb
│   ├── data/
│   ├── notebook_theme.css
│   ├── weatherAUS.csv
│   └── workspace/
├── tests/
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Working Model

Use the repository as an interactive notebook workspace:

1. open the relevant notebook for the topic or homework task
2. execute cells sequentially to reproduce the task setup and experiments
3. complete or review any exercise cells that still contain placeholders
4. compare optimizer behavior, model metrics, generated samples, and visualization outputs
5. use the architecture notes to understand the expected flow before editing a notebook

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
- Some notebooks are active working submissions and may still contain exercise placeholders, downloaded data, or local output state.
