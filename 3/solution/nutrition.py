from scipy.optimize import linprog

result = linprog(
    [1, 3, 2],
    A_ub=[[-3, -8, -1], [-4, 0, -1], [0, -2, -3], 
          [-1, 0, 0], [0, -1, 0], [0, 0, -1]],
    b_ub=[-120, -125, -130, 0, 0, 0]
)

if result.success:
    print(f"Candy Cane: {round(result.x[0], 2)} pounds")
    print(f"Candy Corn: {round(result.x[1], 2)} pounds")
    print(f"Syrup: {round(result.x[2], 2)} pounds")
else:
    print("No solution")