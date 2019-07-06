import math
data = input().split()
n = int(data[0])
m = int(data[1])
ZZ = n/(m+n)*(n-1)/(m+n-1)
ZO = n/(m+n)*(m)/(m+n-1)
OZ = m/(m+n)*(n)/(m+n-1)
OO = m/(m+n)*(m-1)/(m+n-1)

print("X\Y\t0\t1")
print("0\t%.4f\t%.4f"%(OO,ZO))
print("1\t%.4f\t%.4f"%(OZ,ZZ))

