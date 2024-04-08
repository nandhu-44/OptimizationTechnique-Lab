# Simplex Method

import numpy as np
from scipy.optimize import linprog

def simplex(c, A, b, maximize=True):
    c = np.array(c)
    if maximize:
        result = linprog(-c, A_ub=A, b_ub=b, method='highs')
    else:
        result = linprog(c, A_ub=A, b_ub=b, method='highs')
    if result.success:
        return result.x, -result.fun if maximize else result.fun
    else:
        raise Exception('Optimization failed: ' + result.message)

# Maximization
c_max = [3, 2]
A_max = [[1, 4],
         [2, 3]]
b_max = [24, 36]

max_x, max_val = simplex(c_max, A_max, b_max)
print("Maximization Problem:")
print("Optimal Solution:", max_x)
print("Optimal Value:", max_val)

# Minimization
c_min = [2, 3]
A_min = [[-3, -1],
         [-1, -2]]
b_min = [-10, -8]

min_x, min_val = simplex(c_min, A_min, b_min, maximize=False)
print("\nMinimization Problem:")
print("Optimal Solution:", min_x)
print("Optimal Value:", min_val)