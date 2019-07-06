import numpy
import math

data = input().split()
Salary = [float(i) for i in data]
Salary.sort()

R1 = []
for i in range(1,4):
    tempIndex = i * (len(Salary) - 1) / 4
    if tempIndex - int(tempIndex) == 0.5:
        tempResult = (Salary[int(tempIndex)] + Salary[int(tempIndex)+1])/2
        R1.append(tempResult)
    else:
        R1.append(Salary[round(tempIndex)])


R2 = []

for i in range(1,4):
    tempIndex = i * (len(Salary) + 1) / 4 - 1
    if tempIndex - int(tempIndex) == 0.5:
        tempResult = (Salary[int(tempIndex)] + Salary[int(tempIndex)+1])/2
        R2.append(tempResult)
    else:
        R2.append(Salary[round(tempIndex)])

def printList(list):
    for i in range(0,len(list)-1):
        print("%.2f"%list[i],end=" ")
    print("%.2f"%list[-1])

printList(R1)
printList(R2)