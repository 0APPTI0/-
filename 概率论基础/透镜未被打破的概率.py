times = int(input())
result = 1
for i in range(0,times):
    result = result*(1 - (0.4 + 0.1*(i+1)))
if result == -0.0000:
    result = 0.0000


print("%.4f"%result)