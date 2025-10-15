from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver('SCIP')

x1 = solver.IntVar(0, solver.infinity(), 'x1')
x2 = solver.IntVar(0, solver.infinity(), 'x2')

solver.Maximize(4*x1 + 3*x2)

solver.Add(4*x1 + 9*x2 <= 26)
solver.Add(8*x1 + 5*x2 <= 17)

status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print("Value of x1: ",x1.solution_value())
    print("Value of x2: ",x2.solution_value())
    print("Optimal objective value: ", solver.Objective().Value())