import math

def mixedMoment(data, k: int, l: int):
    R = 0
    for a in data:
        R += math.pow(a[0],k)*math.pow(a[1],l)
    return R/len(data)


def mixedCentralMoment(data, k: int, l: int):
    EX = 0
    EY = 0
    for a in data:
        EX += a[0]
        EY += a[1]
    EX /= len(data)
    EY /= len(data)

    R = 0

    for b in data:
        R += math.pow(b[0]-EX,k)*math.pow(b[1]-EY,l)
    return R/len(data)


x = map(float, input().split())
y = map(float, input().split())

points = list(zip(x, y))

while True:
    try:
        k, l = map(int, input().split())
        print('{:.4f} {:.4f}'.format(
            mixedMoment(points, k, l),
            mixedCentralMoment(points, k, l)))
    except EOFError:
        break
