import math

D1 = [float(i) for i in input().split()]
D2 = [float(i) for i in input().split()]

R1 = 0
R2 = 0
R3 = 0
for i in range(0,len(D1)):
    R1 += D1[i] * D2[i]
    R2 += math.pow(D1[i],2)
    R3 += math.pow(D2[i],2)
print("%.4f"%(R1/(math.pow(R2*R3,1/2))))