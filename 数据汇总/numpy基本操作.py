import numpy

size = int(input())

list = input().split()

list0 = [int(i) for i in list]

list1 = numpy.zeros(size)

list2 = numpy.arange(0,size*0.2,0.2)

list3 = numpy.linspace(0,2,size)

numpy.random.seed(size)

list4 = numpy.random.random(size)*2 +1

if len(list0)!=len(list1) or len(list2)!=len(list1) or len(list2)!=len(list3) or len(list3)!=len(list4):
    list2 = list2[0:6]
L = list0+list1+list2+list3+list4

a = numpy.asarray(L)

b = a.reshape(2,int(len(L)/2))

print("ndim: "+str(b.ndim)+", shape: "+str(b.shape)+", size: "+str(b.size)+", itemsize: "+str(b.itemsize)+", dtype: "+str(b.dtype))


print(b)
