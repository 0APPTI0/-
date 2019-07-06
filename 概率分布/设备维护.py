from scipy import stats
import numpy as np
import math
n = int(input())

k = 1
flag = True
if n == 0:
    flag = False
    k = 0
while flag:
    # 同时坏掉个数<=k
    p = stats.binom.pmf(np.arange(0, k+1, 1), n, 0.01)
    P = sum(p)

    if sum(p) > 0.99:
        break
    k += 1

print(k)