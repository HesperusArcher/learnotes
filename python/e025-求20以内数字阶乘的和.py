# -*- coding: utf-8 -*-

# 题目：求1+2!+3!+...+20!的和。

# 程序分析：此程序只是把累加变成了累乘。


# use func fact to solve by myself

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

s=0

for i in range(1,21):
    s+=fact(i)
print(s)

# 此例只为求和，无需计算并保留每一步阶乘值，此方法应当不如 example 1高效


# example 1:

n=0
s=0
t=1
for n in range(1,21):
    t*=n
    s+=t
print(s)

# 此例利用阶乘的性质，逐次将t替代为 (t-1) 的阶乘值


# example 2:

s=0
l=range(1,21)

def op(x):
    r=1
    for i in range(1,x+1):
        r*=i
    return r

s=sum(map(op,l))
print(s)
