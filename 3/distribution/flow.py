from scipy.optimize import linprog

result = linprog(
    [],
    A_ub=[],
    b_ub=[]
)

if result.success:
    edges = ["SA", "SB", "AB", "AT", "BT"]
    for i, edge in enumerate(edges):
        print(f"{edge}: {round(result.x[i])}")
else:
    print("No solution")