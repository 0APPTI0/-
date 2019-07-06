import math
n = int(input())
StringHitRate = input().split()
HitRate = [float(i) for i in StringHitRate]
StringDamage = input().split()
Damage = [float(i) for i in StringDamage]
Aim = int(input())

result = 0

for i in range(int(math.pow(2,n))):
    totalDamage = 0
    totalRate = 1
    recentNum = i
    for j in range(n):
        if recentNum % 2 == 0:
            totalDamage += Damage[j]
            totalRate *= HitRate[j]
        else:
            totalRate *= 1 - HitRate[j]
        recentNum = recentNum // 2
    if totalDamage >= Aim:
        result += totalRate

print("%.4f" %result)