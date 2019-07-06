import math

def mixedCentralMoment(data, k: int, l: int):
    EX = 0
    EY = 0
    for a in data:
        EX += a[0]
        EY += a[1]
    EX /= len(data)
    EY /= len(data)

    R = 0

    for b in data:
        R += math.pow(b[0]-EX,k)*math.pow(b[1]-EY,l)
    return R/len(data)

def B(k: int, x:list):
    A1 = sum(x)/len(x)
    R = 0
    for i in x:
        R += math.pow(i-A1,k)
    Result = R/len(x)
    if round(Result,4) == 0.0000:
        Result = abs(Result)
    return Result

x = map(float, input().split())
y = map(float, input().split())

points = list(zip(x, y))

COV = mixedCentralMoment(points,1,1)

EX = 0
EY = 0
for i in points:
    EX += i[0]
    EY += i[1]
EX /= len(points)
EY /= len(points)
BX = 0
BY = 0
for i in points:
    BX += math.pow(i[0]-EX,2)
    BY += math.pow(i[1]-EY,2)
BX = math.pow(BX/len(points),1/2)
BY = math.pow(BY/len(points),1/2)

PXY = COV/(BY*BX)


print("%.4f %.4f"%(COV,PXY))