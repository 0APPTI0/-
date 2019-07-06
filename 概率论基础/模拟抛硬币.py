# 题目描述
#
# 抛掷一枚质地均匀的硬币，它可能出现正面或者出现反面。请你在随机数种子为 0 下模拟抛硬币，试求正反面出现的频率之差连续五次小于 x 时，总共抛掷的次数。
#
# 输入描述
#
# 输入为一个浮点数 x。
#
# 输出描述
#
# 输出总共抛掷的次数。
#
# 测试样例
#
# 样例1: 输入-输出-解释
#
# 0.1
# 46
# 抛到第 41 次到第 46 次，正反面的总出现次数如下：
# 23 18
# 23 19
# 23 20
# 24 20
# 24 21
# 24 22
# 可以看到，第 42 次到第 46 次，正反面出现的频率之差均小于 0.1，
# 因此总共抛掷 46 次。
# 样例2: 输入-输出
#
# 0.01
# 660
# 注
#
# 请使用内置的 random 库和 randint() 函数。
import random

random.seed(0)

x = float(input())

positiveSideTimes = 0
negativeSideTimes = 0
SimilarTimes = 0
flag = True
while flag:
    if random.random()<0.5:
        positiveSideTimes += 1
    else:
        negativeSideTimes += 1
    if -x<(positiveSideTimes-negativeSideTimes)/(positiveSideTimes+negativeSideTimes)<x:
        SimilarTimes += 1
    else:
        SimilarTimes = 0
    if SimilarTimes == 5:
        flag = False
print(positiveSideTimes+negativeSideTimes)