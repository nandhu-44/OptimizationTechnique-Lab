from scipy.optimize import linprog

c = [-200, -150]
A = [
    [-1, 0],
    [0, -1],
    [-20, -10],
    [-10, -15]
]
b = [-20, -10, -1200, -600]
x_bounds = (0, None)
y_bounds = (0, None)

result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

optimal_acres_wheat = result.x[0]
optimal_acres_barley = result.x[1]
max_profit = -result.fun

print(f"Wheat acres: {optimal_acres_wheat:.2f} acres")
print(f"Barley acres: {optimal_acres_barley:.2f} acres")
print(f"Total profit: ${max_profit:.2f}")
