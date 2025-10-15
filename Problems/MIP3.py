from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver('SCIP')

x1 = solver.IntVar(0, solver.infinity(), 'x1')
x2 = solver.IntVar(0, solver.infinity(), 'x2')

solver.Maximize(2*x1 + 3*x2)

solver.Add(x1 + 2*x2 <= 10)
solver.Add(3*x1 + 4*x2 <= 25)

status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print('x1 =', x1.solution_value())
    print('x2 =', x2.solution_value())
    print('Optimal objective value =', solver.Objective().Value())