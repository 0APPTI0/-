import math


def pnorm(X, p):
    LP = 0
    if p != 'inf' and p != 1:
        for i in X:
            LP += math.pow(i,p)
        LP = math.pow(LP,1/p)
    elif p == 1:
        for i in X:
            LP += abs(i)
    else:
        X1 = []
        for i in X:
            X1.append(abs(i))
        LP = max(X1)

    return LP


X = list(map(float, input().split()))

p = input()
p = int(p) if p != 'inf' else p

print('{:.4f}'.format(pnorm(X, p)))
