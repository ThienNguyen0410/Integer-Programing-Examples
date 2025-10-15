from pyscipopt import Model

scip = Model()
x = scip.addVar(vtype='I', name ='x', lb=0)
y = scip.addVar(vtype='I', name = 'y', lb=0)
z = scip.addVar(vtype='I', name = 'z')
#Add constraints
cons_1 = scip.addCons(x+y <= 5, name="cons 1")
objective = (x-2)**2 + (y-3)**2
cons2 = scip.addCons(z >= objective ,name ="cons 2")


scip.setObjective(z, sense="minimize")
scip.optimize()

if scip.getStatus() == "optimal":
    print("Status:", scip.getStatus())
    print("x =", scip.getVal(x))
    print("y =", scip.getVal(y))
    print("Objective =", scip.getObjVal())
else:
    print("Can not find optimal solution")

