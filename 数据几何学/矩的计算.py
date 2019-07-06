import math

def A(k: int, x):
    R = 0
    for i in x:
        R += math.pow(i,k)

    return R/len(x)


def B(k: int, x):
    A1 = sum(x)/len(x)
    R = 0
    for i in x:
        R += math.pow(i-A1,k)
    Result = R/len(x)
    if round(Result,4) == 0.0000:
        Result = abs(Result)
    return Result


x = list(map(float, input().split()))
for k in range(1, 5):
    print('{:.4f} {:.4f}'.format(A(k, x), B(k, x)))
