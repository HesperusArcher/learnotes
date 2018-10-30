# -*- coding: utf-8 -*-

# method 1:

num=[]
i=2
for i in range(2,100):
    j=2
    for j in range(2,i):
        if (i%j==0):
            break
    else:
        num.append(i)
print(num)

# method 2:
# filter object at

# import math
# def func_get_prime(n):
#     return filter(lambda x: not [x%i for i in range(2, int(math.sqrt(x))+1) if x%i == 0], range(2, n+1))
# print(func_get_prime(100))
