# 题目描述
# 首先构建两个数组：
#
# 使用输入的数组构建一个大小为 size 的数组 a1；
# 使用 size 为随机数种子，构建一个大小为 size，范围在 [0, 10) 的平均分布随机整数数组 a2
# 并将 a1，a2 均重构为 2x(size//2) 的二维数组。
#
# 然后输出：
#
# a1 的元素和、最小值和最大值；
# a1+a2、a1*a2 以及 a1**a2 的结果；
# a2 的转置 和 a1 矩阵乘法的结果；

# 输入描述
# 输入包括两行。第一行为数组的大小 size（偶数）；第二行为任务 1 中的整数数组，大小为 size，两两间用空格隔开。
#
# 输出描述
# 输出请参考测试样例。
#
# 测试样例
# 样例1: 输入
# 6
# 1 9 7 2 3 1
# 样例1：输出
# sum: 23, min: 1, max: 9
# a1 + a2:
#  [[10 12 11]
#  [ 2 12  2]]
# a1 * a2:
#  [[ 9 27 28]
#  [ 0 27  1]]
# a1 ** a2:
#  [[    1   729  2401]
#  [    1 19683     1]]
# a2.T x a1:
#  [[ 9 81 63]
#  [21 54 30]
#  [ 6 39 29]]
# 说明
# 输出数组的第一行首有一个空格。可以类似 print('a:\n', xxx) 这样输出。


import numpy
size = int(input())
list1Temp = input().split()
list1 = [int(i) for i in list1Temp]
numpy.random.seed(size)
list2 = numpy.random.randint(0,10,size)
arr1 = numpy.asarray(list1)
arr2 = numpy.asarray(list2)
A1 = arr1.reshape(2,int(size/2))
A2 = arr2.reshape(2,int(size/2))


print("sum: "+str(A1.sum())+", min: "+str(A1.min())+", max: "+str(A1.max()))

print("a1 + a2:")
print("",end=" ")
print(numpy.add(A1,A2))

print("a1 * a2:")
print("",end=" ")
print(numpy.multiply(A1,A2))

print("a1 ** a2:")
print("",end=" ")
print(numpy.power(A1,A2))

print("a2.T x a1:")
print("",end=" ")
A2=A2.T
print(numpy.dot(A2,A1))