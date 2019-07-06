import random
data = input().split()
n = int(data[0])
m = int(data[1])

a = m + n/(n+m)
b = n + m/(n+m)

print("%.4f"%(a/(a+b)))