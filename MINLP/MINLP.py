import math
from pyscipopt import Model, quicksum


def MINLP_Research():
    num_nodes = int(input("Number of node:"))
    model = Model("MINLP_Research")

    # Parameters
    C = [100 + 10*i for i in range(num_nodes)]
    p = [0.9 + 0.01*i for i in range(num_nodes)]
    B = [50 + 5*i for i in range(num_nodes)]
    S_A = 1000
    S_H = 100
    N_min_hot = 3
    tau_H = 0.05
    tau_A = 0.1
    gamma = 0.8
    T_max = 50
    M = 1e6

    # Variables
    optimal_solution = model.addVar(vtype="C", name="optimal_solution")
    n = model.addVar("n", vtype="I", lb=1)
    k = model.addVar("k", vtype="I", lb=1)
    x = [model.addVar(f"x_{i}", vtype="B") for i in range(num_nodes)]
    z = [model.addVar(f"z_{i}", vtype="B") for i in range(num_nodes)]
    y = [model.addVar(f"y_{i}", vtype="B") for i in range(num_nodes)]
    T_download = model.addVar("T_download", vtype="C",lb=0)


    #-----------------------------Add constraints----------------------

    #Constraint C1
    model.addCons(k <= n-1, name="C1")
    
    #Constraint C2
    model.addCons(quicksum(x[i] for i in range (num_nodes)) == n, name="Constrains C2")

    #Constraint C3
    for i in range(num_nodes):
        model.addCons(x[i] + z[i] <= 1, name=f"C3_node_{i}")

    #Constraint C4
    for i in range(num_nodes):
        model.addCons(z[i]*S_H + (x[i]*S_A)/k <= C[i], name=f"C4_node_{i}")
        
    #C5 constraint
    tmp = quicksum(z[j]*p[j] for j in range(num_nodes))
    tmp -= N_min_hot
    tmp +=1
    model.addCons(2*(tmp)**2 >= -math.log(tau_H)* quicksum(z[i] for i in range(num_nodes)), name="C5")

    #C6 constraint
    tmp_7 = quicksum(x[i]*p[i] for i in range(num_nodes)) -k + 1
    tmp_7 = 2 * (tmp_7)**2
    model.addCons(tmp_7 >= -math.log(tau_A)*n, name="C6")
    

    #C7 constraint
    model.addCons(quicksum(y[i] for i in range(num_nodes)) == k, name="C7")
    
    #C8 constraint
    for i in range(num_nodes):
        model.addCons(y[i] <= x[i], name=f"C8_node_{i}")
    
    #C9 constraint
    for i in range(num_nodes):
        model.addCons(T_download >= S_A/(k*B[i]) - M*(1-y[i]), name=f"C9_node_{i}")

    # C10 constraint
    model.addCons(T_download + (S_A/k)*gamma <= T_max)

    # Build objective function
    objective = n*(S_A/k) + quicksum(z[i]*S_H for i in range(num_nodes))
    model.addCons(optimal_solution >= objective, name="optimal_solution")

    model.setObjective(optimal_solution, sense="minimize")
    model.optimize()
    
    if model.getStatus() == "optimal":
        print("Objective =", model.getObjVal())
    else:
        print("Can not find optimal solution")
    
if __name__ == "__main__":
    MINLP_Research()
