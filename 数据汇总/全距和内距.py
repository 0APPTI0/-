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

Q = max(Salary) - min(Salary)
N = R1[-1] - R1[0]


print("%.2f %.2f"%(Q,N))