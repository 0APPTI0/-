import math
def getC(m,n):
    A = math.factorial(n)/math.factorial(n-m)
    C = A/math.factorial(m)
    return C

n = int(input())
R = []
for i in range(0,n+1):
    R.append(getC(i,n)/math.pow(2,n))

for i in range(0,n):
    print("%.4f"%R[i],end=" ")
print("%.4f"%R[-1])