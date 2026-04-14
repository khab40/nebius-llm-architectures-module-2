# Changelog

## 2026-04-14

- Renamed homework notebooks to shorter `HW*` filenames and registered the new notebook files in git.
- Completed CIFAR-10 submission work, including dataset handling, model training code, Task 1.4/1.5 experiment notebooks, Task 3 experiment notebook, MLP/CNN comparisons, plots, and conclusions from executed results.
- Completed the RNN language-model submission notebook with Apple Silicon device setup, dataset/dataloader implementation, one-hot encoding, LSTM training, sampling strategies, beam search, plots/outputs, and conclusions from executed results.
- Completed both Week 4 bonus submission notebooks:
  - `HW4_bon_p2_forward_sub.ipynb`: forward-pass layers, sigmoid, network assembly, Apple Silicon availability check, smoke experiment, plot, and conclusions.
  - `HW4_bon_p1_backward_sub.ipynb`: backward-pass layers, log loss, full-batch training, mini-batch SGD, MNIST/digits smoke experiment, plots, and conclusions from executed results.
- Migrated dependency management from `requirements.txt` to `uv`, including `pyproject.toml` dependencies, `uv.lock`, README setup commands, and ignored generated package metadata.
- Reorganized notebooks into homework-specific folders under `src/hw1`, `src/hw2`, and `src/hw4`, while keeping practice notebooks at `src/`.
- Moved documentation assets from `src/` to `docs/` and updated notebook/README references for GIF, PDF, text, and CSV data paths.
- Added HW4-focused architecture notes in `docs/architecture` for CIFAR-10 classification, RNN language modeling, the NumPy forward-pass framework, and the NumPy backward-pass framework.
- Updated repository architecture notes and README links to match the new grouped notebook layout and current project contents.
