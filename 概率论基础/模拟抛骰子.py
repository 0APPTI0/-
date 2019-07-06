import random

random.seed(0)

times = int(input())

seZi = [0,0,0,0,0,0]

for i in range(0,times):
    temp = random.randint(1,6)
    values = [1,2,3,4,5,6]
    for j in range(0,6):
        if temp<=values[j]:
            seZi[j]+=1
            break

Result = []
for i in seZi:
    Result.append(i/times)


for i in range(0,len(Result)-1):
    print("%.2f"%Result[i],end=" ")
print("%.2f"%Result[-1])