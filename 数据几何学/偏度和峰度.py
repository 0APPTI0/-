import math

data = input().split()
Salary = [float(i) for i in data]

# Var
def B(k: int, x):
    A1 = sum(x)/len(x)
    R = 0
    for i in x:
        R += math.pow(i-A1,k)
    Result = R/len(x)
    if round(Result,4) == 0.0000:
        Result = abs(Result)
    return Result


B3 = B(3,Salary)/math.pow(B(2,Salary),1.5)
B4 = B(4,Salary)/math.pow(B(2,Salary),2)

print("%.4f %.4f"%(B3,B4))