from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver('SCIP')

x1 = solver.IntVar(0, solver.infinity(), 'x1')
x2 = solver.IntVar(0, solver.infinity(), 'x2')

solver.Maximize(4*x1 + 5*x2)

solver.Add(x1 + 4*x2 >= 5)
solver.Add(3*x1 + 2*x2 >= 7)

status = solver.Solve()
if status == pywraplp.Solver.OPTIMAL:
    print("Value of x1: ",x1.solution_value())
    print("Value of x2: ",x2.solution_value())
    print("Optimal objective value: ", solver.Objective().Value())

elif status == pywraplp.Solver.FEASIBLE:
    print("Value of x1: ",x1.solution_value())
    print("Value of x2: ",x2.solution_value())

elif status == pywraplp.Solver.UNBOUNDED:
    print("Area is unbounded")

elif status == pywraplp.Solver.INFEASIBLE:
    print("No solution")
    
else:
    print("Error")