from pyscipopt import Model

# Tạo model
model = Model("Example")

# # Biến
# x = model.addVar("x", vtype="C")   # Continuous
# y = model.addVar("y", vtype="C")

# # Hàm mục tiêu
# model.setObjective(3*x + 2*y, sense="maximize")

# # Ràng buộc
# model.addCons(x + y <= 4)
# model.addCons(x <= 2)
# model.addCons(y <= 3)

# # Giải
# model.optimize()

# # In kết quả
# print("Optimal value:", model.getObjVal())
# print("x =", model.getVal(x))
# print("y =", model.getVal(y))
x = model.addVar("x")
y = model.addVar("y")
z = model.addVar("z")

model.addCons(x**2 + y**2 <= 10)  # ràng buộc phi tuyến
objective = x*y
model.addCons(z <= objective)
model.setObjective(z, "maximize")
model.optimize()

if model.getStatus() == "optimal":
    print("Status:", model.getStatus())
    print("x =", model.getVal(x))
    print("y =", model.getVal(y))
    print("Objective =", model.getObjVal())

else:
    print("Can not find optimal value")
