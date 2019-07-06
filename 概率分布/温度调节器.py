from scipy.stats import norm
data = input().split()
c = int(data[0])
p = float(data[1])


a = norm.ppf(p,0,1)

R = c + a*0.5

print("%.2f"%R)