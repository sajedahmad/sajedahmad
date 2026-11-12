import numpy as np

from paper.allocation import cost_matrix, greedy_allocation, total_cost


def test_greedy_assigns_each_task_once():
    costs = np.array([[1.0, 5.0], [4.0, 2.0]])
    assignment = greedy_allocation(costs)
    assert assignment == {0: 0, 1: 1}
    assert total_cost(costs, assignment) == 3.0


def test_cost_matrix_shape():
    robots, tasks = np.zeros((3, 2)), np.ones((4, 2))
    assert cost_matrix(robots, tasks).shape == (3, 4)
