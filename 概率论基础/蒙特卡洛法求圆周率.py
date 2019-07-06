import random as R
times = int(input())
R.seed(0)



Times = 0
for i in range(0,times):
    a = R.random()
    b = R.random()
    if pow(a,2)+pow(b,2)<=1:
        Times += 1

Pi = 4*Times/times

print("%.4f"%Pi)
