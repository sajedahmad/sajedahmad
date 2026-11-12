# Guidance for Claude Code

This repo is the GitHub profile repo: the root `README.md` is the public profile page. Don't edit it unless asked.

The paper's Python code lives in `paper/`. Run all commands from there.

- Install / sync deps: `uv sync` (add a dependency with `uv add <pkg>`)
- Run experiments: `uv run python -m paper.run --config configs/default.yaml`
- Tests: `uv run pytest`
- Lint: `uv run ruff check .` (format with `uv run ruff format .`)

Conventions:
- Library code goes in `paper/src/paper/`, experiment settings in `paper/configs/*.yaml`.
- Every experiment takes a seed from its config so results are reproducible.
- Outputs go to `paper/results/` and raw data to `paper/data/`; neither is committed.
