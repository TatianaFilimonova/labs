import numpy
import xlrd
from scipy.optimize import linprog

var = int(input("Enter the number of your option: "))
n = var + 1

yrojai = []
available = []
profit = []
prod_name = []
rb = xlrd.open_workbook(r'FARMER.xls', formatting_info=True)
sheet = rb.sheet_by_index(0)
k = 1
for i in range(k, k+6):
    yrojai.append(sheet.row_values(n)[i])
k += 6
for i in range(k, k+6):
    available.append(sheet.row_values(n)[i])
k += 6
for i in range(k, k+6):
    profit.append(sheet.row_values(n)[i])
for i in range(1, 7):
    prod_name.append(sheet.row_values(1)[i])

cost = [0 for k in range(6)]  # стоит 1 га урожая
for i in range(6):
    cost[i] = -1 * yrojai[i] * profit[i]

tot1_eq = numpy.ones([1, len(cost)])
tot2_eq = [10]

tot1_ub = numpy.zeros([len(cost), len(cost)])
for i in numpy.arange(0, len(cost), 1):
    for j in numpy.arange(0, len(cost)):
        if i == j:
            tot1_ub[i, j] = 1

opt = linprog(cost, tot1_ub, available, tot1_eq, tot2_eq, method='highs-ds')

print('Total profit:', opt.fun * (-1))

print('You need to plant:')
for i in range(len(opt.x)):
    if opt.x[i] != 0:
        print(prod_name[i], ': ', round(opt.x[i], 1), 'hа')  # без округления косячит картошка :(
