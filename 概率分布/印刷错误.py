import math
from scipy import stats
import scipy.stats as st
import numpy as np

def getC(m,n):
    A = math.factorial(n)/math.factorial(n-m)
    C = A/math.factorial(m)
    return C

data = input().split()
p = float(data[0])
n = int(data[1])

p1 = stats.binom.pmf(np.arange(0, 2+1, 1), n, p)
P = sum(p1)

print("%.6f"%P)

#
# # P(x=k),a为指数函数的参数
# def Poission(k,a):
#     return math.pow(a,k)*math.pow(math.e,-a)/math.factorial(k)
a = n*p
P1 = math.exp(-a) + a*math.exp(-a) + math.pow(a,2)*math.exp(-a)/2

print("%.6f"%P1)