from ortools.linear_solver import pywraplp

def IP_example4():
    solver = pywraplp.Solver.CreateSolver('SCIP')

    x = {}
    for i in range (0,5):
        for j in range (0,5):
            x[i,j] = solver.BoolVar(f'x{i}{j}')

    y = {}
    for i in range (1,5):
        y[i] = solver.BoolVar(f'y{i}')

    #Add constraints
    for i in range (1,5):
        solver.Add(x[i,1] + x[i,2] + x[i,3] + x[i,4] == 1)

    for i in range (1,5):
        for j in range (1,5):
            solver.Add(x[j,i] <= y[i])

    z = solver.Sum([
        28*x[1,1] + 84*x[1,2] + 112*x[1,3] + 112*x[1,4] +
        60*x[2,1] + 20*x[2,2] + 50*x[2,3] + 50*x[2,4] +
        96*x[3,1] + 60*x[3,2] + 24*x[3,3] + 60*x[3,4] +
        64*x[4,1] + 40*x[4,2] + 40*x[4,3] + 16*x[4,4] +
        50*y[1] + 50*y[2] + 50*y[3] + 50*y[4]
    ])

    solver.Minimize(z)
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print("Result example 4:")
        print("Optimal value Z = ", solver.Objective().Value())
        for i in range (1,5):
            for j in range (1,5):
                print(f"{x[i,j].name()} = {x[i,j].solution_value()}")
        
        for i in range (1,5):
            print(f"{y[i].name()} = {y[i].solution_value()}")
    else:
        print("Can not find optimal solution")

if __name__ == "__main__":
    IP_example4()