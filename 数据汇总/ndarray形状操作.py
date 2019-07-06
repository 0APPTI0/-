# 题目描述
# NumPy 提供了多种机制，可以让使用者方便地转换 array 的形状。
#
# 任务 1 ：构建一个 3*4、范围在 [0, 20) 的随机整数数组 a；
#
# 拆分数组
# 任务 2 ：用 hsplit 将 a 按行分成两个 array，分别为 ha1, ha2；
#
# 任务 3 ：用 vsplit 将 a 按列分成三个 array，分别为 va1, va2 和 va3；
#
# 拼接数组
# 任务 4 ：用 hstack 将 ha1 和 ha2 在水平方向上拼接成一个数组；
#
# 任务 5 ：用 vstack 将 va1 和 va2 在垂直方向上拼接成一个数组；
#
# “拉平” 数组
# 任务 6 ：尝试使用 reshape，ravel 和 flatten 将 a 变成 1*12 的形状。
#
# 输入描述
# 输入为一个整数，表示随机数种子。
#
# 输出描述
# 请在输入的随机数种子下，输出：
#
# 任务 1 构成的随机整数数组；
# 任务 2 中的 ha1；
# 任务 3 中的 va1；
# 任务 4 的结果；
# 任务 5 的结果；
# 任务 6 中的结果；
# 格式参数测试样例。
#
# 测试样例
# 样例1: 输入-输出
# 0
# a:
#  [[12 15  0  3]
#  [ 3  7  9 19]
#  [18  4  6 12]]
# ha1:
#  [[12 15]
#  [ 3  7]
#  [18  4]]
# va1:
#  [[12 15  0  3]]
# hstack:
#  [[12 15  0  3]
#  [ 3  7  9 19]
#  [18  4  6 12]]
# vstack:
#  [[12 15  0  3]
#  [ 3  7  9 19]]
# a:
#  [12 15  0  3  3  7  9 19 18  4  6 12]
# 说明
# 输出数组的第一行首有一个空格。可以类似 print('a:\n', xxx) 这样输出。

import numpy

Seed = int(input())
numpy.random.seed(Seed)

a = numpy.random.randint(0,20,12)
b = a
a = a.reshape(3,4)
# print("a:")
# print("",end=" ")
# print(a)

ha = numpy.hsplit(a,2)

va = numpy.vsplit(a,(1,2))

HS = numpy.hstack((ha[0],ha[1]))

VS = numpy.vstack((va[0],va[1]))

print("a:")
print("",end=" ")
print(a)

print("ha1:")
print("",end=" ")
print(ha[0])

print("va1:")
print("",end=" ")
print(va[0])

print("hstack:")
print("",end=" ")
print(HS)

print("vstack:")
print("",end=" ")
print(VS)

print("a:")
print("",end=" ")
print(b)