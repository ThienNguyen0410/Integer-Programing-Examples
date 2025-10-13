from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver('SCIP')

#Declare variables
x = {}
for i in range (1,4):
    x[i] = solver.IntVar(0,solver.infinity(),f'x{i}')

y = {}
for j in range (1,4):
    y[j] = solver.BoolVar(f'x{j}')

# Add constraints
for i in range(1,4):
    solver.Add(x[i] <= 2000*y[i])
    solver.Add(1000 - x[i] <= 2000*(1-y[i]))
solver.Add(1.5*x[1] + 3*x[2] + 5*x[3] <= 6000)
solver.Add(30*x[1] + 25*x[2] + 40*x[3] <= 60000)
solver.Maximize(2*x[1] + 3*x[2] + 4*x[3])

status = solver.Solve()
if status == pywraplp.Solver.OPTIMAL:
    print("Result of example 6:")
    print(f"Optimal value z   = {solver.Objective().Value()}")
    for i in range(1,4):
        print(f"{x[i].name()} = {x[i].solution_value()}")
    
    for i in range(1,4):
        print(f"{y[i].name()} = {y[i].solution_value()}")
    