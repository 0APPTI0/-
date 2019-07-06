import math
from scipy import integrate


data = input().split()
a = float(data[0])
b = float(data[1])


def F(x):
    return x - math.pow(x,2)
P1 = 0
if a < 1 < b :
    res, err = integrate.quad(F, a, 1)
    S = res
    P1 = 2*S/((a+b)*(b-a))
elif b <= 1:
    res, err = integrate.quad(F, a, b)
    S = res
    P1 = 2 * S /( (a + b) * (b - a))

P2 = 0
if a < 0.3 and b > 0.3:
    res = (a+0.3)*(0.3-a)/((a+b)*(b-a))
    P2 = res
elif b < 0.3:
    P2 = 1

print("%.4f"%P1)
print("%.4f"%P2)