# Paper code

Python project for the paper's experiments (multi-robot task allocation).

## Setup

Uses [uv](https://docs.astral.sh/uv/) for environments and dependencies.

```bash
cd paper
uv sync
```

## Run

```bash
uv run python -m paper.run --config configs/default.yaml
uv run pytest
```

## Layout

- `src/paper/` – library code (methods, simulation, metrics)
- `configs/` – experiment configs (YAML)
- `tests/` – unit tests
- `data/` – input data (not committed)
- `results/` – experiment outputs (not committed)
- `notebooks/` – exploration and figures
