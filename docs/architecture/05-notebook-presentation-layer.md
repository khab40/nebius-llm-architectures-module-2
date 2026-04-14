# Notebook Presentation Layer

The project uses a shared CSS file to provide consistent notebook styling inspired by Nebius Academy and the [Nebius AI Performance Engineering](https://academy.nebius.com/ai-engineering-uk) course materials. This is a presentation architecture choice: styling is centralized in one place instead of being duplicated inside every `.ipynb` file.

## Key idea

Each notebook loads the same stylesheet through a small HTML reference cell. That keeps notebook JSON smaller and makes style changes global.

## Diagram

```mermaid
flowchart LR
    A[Notebook File] --> B[First Markdown Cell]
    B --> C[Stylesheet Link]
    C --> D[Shared Notebook Theme CSS]
    D --> E[Typography]
    D --> F[Colors]
    D --> G[Code Cell Surfaces]
    D --> H[Image and Card Styling]
    E --> I[Consistent Notebook Presentation]
    F --> I
    G --> I
    H --> I
```

## Where it appears

- themed homework/report notebooks under `src/hw*/` begin with a stylesheet reference to `../notebook_theme.css`
- the CSS file defines the Nebius Academy-inspired palette, spacing, card treatment, and output styling

## Relevant files

- [`../../src/notebook_theme.css`](../../src/notebook_theme.css)
- [`../../src/hw2/HW2_Gradient_descent_&_Pytorch.ipynb`](../../src/hw2/HW2_Gradient_descent_&_Pytorch.ipynb)
- [`../../src/hw1/HW_1_sub.ipynb`](../../src/hw1/HW_1_sub.ipynb)
- [`../../src/hw2/pytorch_optimization_report.ipynb`](../../src/hw2/pytorch_optimization_report.ipynb)

## Architectural significance

- avoids repeated inline CSS across notebooks
- makes restyling low-risk and centralized
- keeps visual consistency across lecture, homework, and report artifacts
