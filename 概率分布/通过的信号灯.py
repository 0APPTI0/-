import math
data = input().split()
n = int(data[0])
p = float(data[1])
R = []
R.append(p)
for i in range(1,n):
    R.append(math.pow(1-p,i)*p)
temp = 1
for i in range(0,n):
    temp -= R[i]
R.append(temp)

print("X\t",end="")
for a in range(0,n):
    print(str(a),end="\t")
print(str(n))
print("P\t",end="")
for a in range(0,n):
    print("%.4f"%R[a],end="\t")
print("%.4f"%R[n])

E = 0
V = 0
for i in range(0,n+1):
    E += R[i] * i
    V += R[i] * i * i
V -= E * E



print("%.4f"%E)
print("%.4f"%V)
