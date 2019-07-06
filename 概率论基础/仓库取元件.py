FactoryNumbers = int(input())
temp1 = input().split()
temp2 = input().split()
DefectiveRate = [float(i) for i in temp1]
Proportion = [float(i) for i in temp2]

result1 = 0
for i in range(0,FactoryNumbers):
    result1 += DefectiveRate[i] * Proportion[i]

result2 = []
for i in range(0,FactoryNumbers):
    P = DefectiveRate[i] * Proportion[i] / result1
    result2.append(P)
print("%.4f"%result1)
for i in range(0,FactoryNumbers-1):
    print("%.4f"%result2[i],end=" ")
print("%.4f"%result2[-1])
