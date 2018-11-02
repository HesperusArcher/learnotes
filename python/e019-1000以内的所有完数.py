# -*- coding: utf-8 -*-


# 题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。

# 程序分析：请参照程序Python 练习实例14。

# from sys import stdout

# for j in range(2,1001):
#     k=[]
#     n=-1
#     s=j
#     for i in range(1,j):
#         if j%i==0:
#             n+=1
#             s-=1
#             k.append(i)

#     if s==0:
#         print(j)
#         for i in range(n):
#             stdout.write(str(k[i]))
#             stdout.write(' ')
#         print(k[n])

# python3 未出结果，手算仍不明此算法


# another example:

# 这题只要弄明白“完数”及其“因子”的概念，就不难。一开始我把“因子”理解为“质因子”，结果只算得出个6。后来才知道，只要数字a能被数字b整除，不论b是不是质数，都算是a的因子。比如：8的质因子是 2, 2, 2，但8的因子就包括 1,2,4。

# 这么算来，求解“因子”可就比“质因子”简单多了，因为不用担心质因子重复的问题。代码如下：

import math

for i in range(2,1000):
    factors=[]
    for j in range(1, math.floor(i/2)+1):
        if i%j == 0:
            factors.append(j)
    if sum(factors) == i:
        print(i,end=',')


# third example:

for i in range(2,1000):
    l1 = []
    for j in range(1,i):
        if i%j==0:
            l1.append(j)
    num = sum(l1)
    if num == i:
        print("%d ="%i,)
        for i in range(len(l1)):
            if i == len(l1)-1:
                print(l1[i])
            else:
                print("%d +"%l1[i],)
