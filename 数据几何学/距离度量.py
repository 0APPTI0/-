import math

D1 = [float(i) for i in input().split()]
D2 = [float(i) for i in input().split()]

R1 = 0
for i in range(0,len(D1)):
    R1 += abs(D1[i] - D2[i])

R2 = 0
for i in range(0,len(D1)):
    R2 += math.pow(D2[i] - D1[i],2)
R2 = math.pow(R2,1/2)

R3 = 0
for i in range(0,len(D1)):
    if abs(D2[i] - D1[i]) > R3:
        R3 = abs(D2[i] - D1[i])

print("%.4f %.4f %.4f"%(R1,R2,R3))