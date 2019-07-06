import math
data = input().split()
n = int(data[0])
m = int(data[1])

if n-m>0:
    A = math.factorial(n)/math.factorial(n-m)
    C = A/math.factorial(m)

else:
    A = 0
    C = 0
if m ==0:
    A = 0
    C = 0
elif n == m :
    A = 1
    C = 1


print(int(A),int(C))