import numpy
from scipy import stats
import math

Salary = [float(i) for i in input().split()]

A = sum(Salary)/len(Salary)

G = stats.gmean(Salary)

H = stats.hmean(Salary)

Q = 0
for i in Salary:
    Q += math.pow(i,2)
Q /= len(Salary)
Q = math.pow(Q,1/2)

print("%.4f %.4f %.4f %.4f"%(A,G,H,Q))