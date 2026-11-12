"""Experiment entry point: `uv run python -m paper.run --config configs/default.yaml`."""

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
import yaml

from paper.allocation import cost_matrix, greedy_allocation, random_instance, total_cost


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/default.yaml")
    args = parser.parse_args()

    cfg = yaml.safe_load(Path(args.config).read_text())
    rng = np.random.default_rng(cfg["seed"])

    rows = []
    for trial in range(cfg["trials"]):
        robots, tasks = random_instance(cfg["n_robots"], cfg["n_tasks"], rng)
        costs = cost_matrix(robots, tasks)
        assignment = greedy_allocation(costs)
        rows.append({"trial": trial, "method": "greedy", "cost": total_cost(costs, assignment)})

    out_dir = Path(cfg["output_dir"])
    out_dir.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(rows)
    df.to_csv(out_dir / "results.csv", index=False)
    print(df.groupby("method")["cost"].describe())
    print(f"Saved {out_dir / 'results.csv'}")


if __name__ == "__main__":
    main()
