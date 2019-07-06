import math
data = input().split()
n = int(data[0])
m = int(data[1])
if n+m!=0 and n+m!=1:
    result1 = pow(n/(n+m),2)
    result2 = (n/(n+m)) * ((n-1)/(n+m-1))
elif n==1 and m==0:
    result1 = 1
    result2 = 0
else:
    result2 = 0
    result1 = 0
print("%.4f\n%.4f"%(result1,result2))