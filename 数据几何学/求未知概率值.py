data = input().split()
a = float(data[0])
b = float(data[1])
c = float(data[2])
R1 = [0,0]
R2 = [0,0,0]
R3 = [0,0,0,1]

R3[0] = a + c
R1[1] = a/(a+c)
R1[0] = R1[1] - a - b
R2[-1] = 1 - R1[-1]
R3[1] = b/(1-R2[-1])
R2[0] = R3[1] - b
R2[1] = R2[-1] - c - R2[0]
R3[2] = 1 - R3[0] - R3[1]

print("P(i,j)\tj=0\tj=1\tj=2\tP(i)")
print("i=1\t%.4f\t%.4f\t%.4f\t%.4f"%(a,b,R1[0],R1[1]))
print("i=2\t%.4f\t%.4f\t%.4f\t%.4f"%(c,R2[0],R2[1],R2[2]))
print("P(j)\t%.4f\t%.4f\t%.4f\t%.4f"%(R3[0],R3[1],R3[2],R3[3]))