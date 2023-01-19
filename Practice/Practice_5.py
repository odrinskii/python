 #lambda, filter, map, zip, enumerate, list comprehension

#list comprehension
import random

# a = [i for i in range(1,10) if i%2==0]
# print(a)

#enumerate

# a = [2, 4, 6, 8]
# for indx,val in enumerate(a):
# if val>5:
# a[indx] = 0
# print(a)

#zip
# a = [1,2,3]
# months = ["june","july","july1","july2","july3","july4"]
# dit_s = {1:"ddd",2:"112"}
# result = list(zip(a,months,dit_s))
# print(result[1][1])

#lambda
# def summ(a,b,*args):
# for i in args:
# print(i)
# return a+b
# print(summ(2,3,4,5,6,7))

# summ = lambda a,b: a+b if a>5 else 0
#
# for i in range(10):
# print(summ(7,3))

#map
# a = [(2,4,3),(4,5,6),(1,2,3)]
#
# a = list(map(lambda x:x[0]*x[1]*x[2],a))
# print(a)

#filter
# a = [2,4,3,4,5,6,1,2,3]
#
# res = list(filter(lambda x: True if x%2==0 else False,a))
# print(res)

#sorted
# a = [(6,5,5),(4,5,5),(1,2,3)]
# res = sorted(a,key = lambda x: (x[2],x[1],x[0]),reverse=True)
# print(res)