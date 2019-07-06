from scipy.stats import mode
Salary = [float(i) for i in input().split()]
Salary.sort()

list = []
NO = []
for i in Salary:
    temp = i//3
    if not (temp in list):
        list.append(temp)
        NO.append(1)
    else:
        a = list.index(temp)
        NO[a] += 1

ResultSet = []
a = NO.index(max(NO))
initMax = max(NO)
str1 = "["+str(int(3*list[a]))+","+str(3*(int(list[a]+1)))+")"
ResultSet.append(str1)
NO[a] -= 1

while max(NO) == initMax:
    i = NO.index(max(NO))
    str1 = "[" + str(int(3 * list[i])) + ", " + str(3 * (int(list[i] + 1))) + ")"
    ResultSet.append(str1)
    NO[i] -= 1

# print(list)
# print(NO)
# print(ResultSet)
for i in ResultSet:
    print(i)