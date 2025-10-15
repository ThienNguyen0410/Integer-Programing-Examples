from ortools.linear_solver import pywraplp

# Create the solver.
solver = pywraplp.Solver.CreateSolver('GLOP')

# Create the variables.
x = solver.NumVar(0, 1, 'x')
y = solver.NumVar(0, 2, 'y')

# Define the objective function.
solver.Maximize(x + 2 * y)

# Define the constraints.
solver.Add(x + y <= 2)

# Solve the problem.
status = solver.Solve()

# Display the results.
if status == pywraplp.Solver.OPTIMAL:
    print('Solution:')
    print('x =', x.solution_value())
    print('y =', y.solution_value())
    print('Optimal objective value =', solver.Objective().Value())
else:
    print('The problem does not have an optimal solution.')