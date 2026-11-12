"""Example multi-robot task allocation (MRTA) baseline.

Replace or extend this with the methods from your paper.
"""

import numpy as np


def random_instance(n_robots: int, n_tasks: int, rng: np.random.Generator):
    """Random 2D positions for robots and tasks in the unit square."""
    return rng.random((n_robots, 2)), rng.random((n_tasks, 2))


def cost_matrix(robots: np.ndarray, tasks: np.ndarray) -> np.ndarray:
    """Euclidean distance from every robot to every task, shape (n_robots, n_tasks)."""
    return np.linalg.norm(robots[:, None, :] - tasks[None, :, :], axis=-1)


def greedy_allocation(costs: np.ndarray) -> dict[int, int]:
    """Repeatedly assign the cheapest remaining (robot, task) pair. Returns {task: robot}."""
    costs = costs.astype(float).copy()
    assignment: dict[int, int] = {}
    for _ in range(min(costs.shape)):
        r, t = np.unravel_index(np.argmin(costs), costs.shape)
        assignment[int(t)] = int(r)
        costs[r, :] = np.inf
        costs[:, t] = np.inf
    return assignment


def total_cost(costs: np.ndarray, assignment: dict[int, int]) -> float:
    return float(sum(costs[r, t] for t, r in assignment.items()))
