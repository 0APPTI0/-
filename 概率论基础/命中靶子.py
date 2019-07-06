data = input().split()
HitRate = [float(i) for i in data]

result = 1

for i in HitRate:
    result *= (1 - i)

print("%.4f"%(1-result))