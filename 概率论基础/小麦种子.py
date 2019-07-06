data = input().split()
rate = [float(i) for i in data]
P = (1-sum(rate))*0.5+rate[0]*0.15+rate[1]*0.1+rate[2]*0.05

print("%.4f"%P)