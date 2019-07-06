

import math
def getC(m,n):
    A = math.factorial(n)/math.factorial(n-m)
    C = A/math.factorial(m)
    return C

n = int(input())
P1 = 3 * 0.02 * 0.98 * 0.98

Fake = int(n * 0.02)
Real = n - Fake
# P2 = getC(1,Fake)*getC(2,Real)/getC(3,n)
P3 = (Fake)*(Real*(Real-1)/2)/((n*(n-1)*(n-2))/6)

print("%.6f"%P1)
print("%.6f"%P3)
