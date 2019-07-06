from scipy.stats import norm
data = input().split()
p1 = float(data[0])
p2 = float(data[1])

f1 = norm.ppf(p1,0,1)
f2 = norm.ppf(1-p2,0,1)

O = 50/(f2-f1)
U = 500 - O*f1

print("%.4f %.4f"%(U,O))