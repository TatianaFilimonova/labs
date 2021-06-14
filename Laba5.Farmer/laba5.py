import xlrd
from pulp import *
var = int(input("Enter the number of your option: "))
n = var + 1

Yield = []
available = []
profit = []
# C:\Users\filim\OneDrive\Документы\labs\Laba5.Farmer
rb = xlrd.open_workbook(r'FARMER.xls', formatting_info=True)
sheet = rb.sheet_by_index(0)
k = 1
for i in range(k, k+6):
    Yield.append(sheet.row_values(n)[i])
k += 6
for i in range(k, k+6):
    available.append(sheet.row_values(n)[i])
k += 6
for i in range(k, k+6):
    profit.append(sheet.row_values(n)[i])

carrot = pulp.LpVariable("Carrot", lowBound=0)
cabbage = pulp.LpVariable("Cabbage", lowBound=0)
peas = pulp.LpVariable("Pear", lowBound=0)
potato = pulp.LpVariable("Potato", lowBound=0)
prodM = pulp.LpVariable("Product M", lowBound=0)
Aorange = pulp.LpVariable("A orange", lowBound=0)

problem = pulp.LpProblem('0', LpMaximize)
problem += Yield[0] * profit[0] * carrot + Yield[1] * profit[1] * cabbage + Yield[2] * profit[2] * peas + Yield[3] * profit[3] * potato + Yield[4] * profit[4] * prodM + Yield[5] * profit[5] * Aorange, "sum"
problem += carrot <= available[0], "1"
problem += cabbage <= available[1], "2"
problem += peas <= available[2], "3"
problem += potato <= available[3], "4"
problem += prodM <= available[4], "5"
problem += Aorange <= available[5], "6"
problem += carrot + cabbage + peas + potato + prodM + Aorange <= 10, "max"

problem.solve()
print("Planting in hectares: ")  # сколько чаго сажаем
for variable in problem.variables():
    if variable.varValue != 0:
        print(variable.name, "=", variable.varValue)
print("Profit:")  # сколько деняк получаем
print(value(problem.objective))
