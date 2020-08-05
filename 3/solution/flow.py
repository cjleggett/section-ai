from scipy.optimize import linprog

result = linprog(
    [0, 0, 0, -1, -1],
    A_ub=[[1, 0, 0, 0, 0],
          [0, 1, 0, 0, 0],
          [0, 0, 1, 0, 0],
          [0, 0, 0, 1, 0],
          [0, 0, 0, 0, 1],
          [-1, 0, 1, 1, 0],
          [0, -1, -1, 0, 1]],
    b_ub=[10, 5, 10, 5, 20, 0, 0]
)

if result.success:
    edges = ["SA", "SB", "AB", "AT", "BT"]
    for i, edge in enumerate(edges):
        print(f"{edge}: {round(result.x[i])}")
else:
    print("No solution")