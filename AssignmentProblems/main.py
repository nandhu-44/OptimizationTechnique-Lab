import numpy as np
from scipy.optimize import linear_sum_assignment


def hungarian_assignment(cost_matrix):
    row_indices, col_indices = linear_sum_assignment(cost_matrix)
    total_cost = cost_matrix[row_indices, col_indices].sum()
    return row_indices, col_indices, total_cost


# Example usage:
cost_matrix = np.array(
    [
        [16, 16, 13, 22, 17],
        [14, 14, 13, 19, 15],
        [19, 19, 20, 23, 50],
        [50, 12, 50, 15, 11],
    ]
)

row_indices, col_indices, total_cost = hungarian_assignment(cost_matrix)

print("Optimal Assignment:")
for i, j in zip(row_indices, col_indices):
    print(f"Task {i} -> Worker {j}")

print("Total Cost:", total_cost)
