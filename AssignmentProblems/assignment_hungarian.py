import numpy as np
from typing import Tuple, List


def hungarian_algorithm(cost_matrix: np.ndarray) -> Tuple[List[int], List[int], float]:
    """
    Solves the assignment problem using the Hungarian algorithm (Kuhn-Munkres algorithm)
    Args:
        cost_matrix (numpy.ndarray): A 2D array representing the cost of assignment.
    Returns:
        List[int]: A list of row indices representing the optimal assignment.
        List[int]: A list of column indices representing the optimal assignment.
        float: The total cost of the optimal assignment.
    """
    n = cost_matrix.shape[0]
    cost_matrix = cost_matrix.astype(float)
    row_indices = []
    col_indices = []
    total_cost = 0

    # Subtract the minimum value from each row
    row_min = np.min(cost_matrix, axis=1)[:, np.newaxis]
    cost_matrix -= row_min

    # Create a list of unassigned rows and columns
    unassigned_rows = list(range(n))
    unassigned_cols = list(range(n))

    while unassigned_rows:
        # Find the minimum uncovered value
        min_val = np.inf
        min_row, min_col = None, None
        for row in unassigned_rows:
            for col in unassigned_cols:
                if cost_matrix[row, col] < min_val:
                    min_val = cost_matrix[row, col]
                    min_row, min_col = row, col

        # Add the minimum value to all uncovered rows and subtract it from all uncovered columns
        for row in unassigned_rows:
            cost_matrix[row] += min_val
        for col in unassigned_cols:
            cost_matrix[:, col] -= min_val

        # Mark the minimum value as covered
        cost_matrix[min_row, min_col] = np.inf

        # Update the assignment and total cost
        row_indices.append(min_row)
        col_indices.append(min_col)
        total_cost += min_val

        # Remove the assigned row and column from unassigned lists
        unassigned_rows.remove(min_row)
        unassigned_cols.remove(min_col)

    # Subtract the row minimum values from the total cost
    total_cost += np.sum(row_min)

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

row_indices, col_indices, total_cost = hungarian_algorithm(cost_matrix)
print("Optimal Assignment:")
for i, j in zip(row_indices, col_indices):
    print(f"Task {i} -> Worker {j}")
print("Total Cost:", total_cost)
