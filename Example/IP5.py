
from ortools.linear_solver import pywraplp
def IP_example5():
    solver = pywraplp.Solver.CreateSolver('SCIP')

    #Declare all variables 
    x = {}
    for i in range (1,7):
        x[i] = solver.BoolVar(f'x{i}')

    #Add Constraints
    solver.Add(x[1] + x[2] >= 1)
    solver.Add(x[1] + x[2] + x[6] >= 1)
    solver.Add(x[3] + x[4] >= 1)
    solver.Add(x[3] + x[4] + x[5] >= 1)
    solver.Add(x[4] + x[5] + x[6] >= 1)
    solver.Add(x[2] + x[5] + x[6] >= 1)

    z = solver.Sum([x[1] + x[2] + x[3] + x[4] + x[5] + x[6]])
    solver.Minimize(z)

    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print("Result of example 5:")
        print(f"Objective value z = {solver.Objective().Value()}")
        for i in range (1,7):
            print(f"{x[i].name()} = {x[i].solution_value()}")

if __name__ == "__main__":
    IP_example5()
    