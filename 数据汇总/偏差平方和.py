import numpy,math
Salary = [float(i) for i in input().split()]
Salary.sort()
SalaryVar = numpy.var(Salary)
A = SalaryVar * len(Salary)
B = math.pow(SalaryVar,1/2)

print("%.2f %.2f %.2f"%(A,SalaryVar,B))

