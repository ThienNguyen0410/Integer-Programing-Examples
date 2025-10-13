from ortools.linear_solver import pywraplp

def IP_example3():
    # Creat Solver
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        print("SCIP solver not found!")
        return

    # Integer variables x1,x2,x3 >= 0
    x1 = solver.IntVar(0, solver.infinity(), 'x1')
    x2 = solver.IntVar(0, solver.infinity(), 'x2')
    x3 = solver.IntVar(0, solver.infinity(), 'x3')

    # Binary variables y1,y2,y3
    y1 = solver.BoolVar('y1')
    y2 = solver.BoolVar('y2')
    y3 = solver.BoolVar('y3')

    # Big M
    M1, M2, M3 = 40, 53, 25

    # Add constraints
    solver.Add(4*x1 + 3*x2 + 4*x3 <= 160)
    solver.Add(3*x1 + 2*x2 + 6*x3 <= 150)

    # Big-M linking constraints
    solver.Add(x1 <= M1 * y1)
    solver.Add(x2 <= M2 * y2)
    solver.Add(x3 <= M3 * y3)

    # ----- OBJECTIVE FUNCTION -----
    # max z = 6x1 + 4x2 + 7x3 - 200y1 - 150y2 - 100y3
    objective = (
        6*x1 + 4*x2 + 7*x3
        - 200*y1 - 150*y2 - 100*y3
    )
    solver.Maximize(objective)

    # ----- SOLVE -----
    status = solver.Solve()

    # ----- RESULT -----
    if status == pywraplp.Solver.OPTIMAL:
        print("Result of example 3:")
        print("Optimal solution found:")
        print(f"z = {solver.Objective().Value()}")
        print(f"x1 = {x1.solution_value()}")
        print(f"x2 = {x2.solution_value()}")
        print(f"x3 = {x3.solution_value()}")
        print(f"y1 = {y1.solution_value()}")
        print(f"y2 = {y2.solution_value()}")
        print(f"y3 = {y3.solution_value()}")
    else:
        print("No optimal solution found")

if __name__ == "__main__":
    IP_example3()
