# -*- coding: utf-8 -*-

# 题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。

# 程序分析：请抓住分子与分母的变化规律。


# use fibonacci to solve by myself

def fib(n):
    if n<=2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

# j=0
k=[]

for i in range(1,21):
    s=fib(i+2)/fib(i+1)
    k.append(s)
    # j+=s # 仅求和，可不列出各项值仅做累加，以j代替k

print(sum(k))
# print(j)


# example 1:

a=2.0
b=1.0
s=0
for n in range(1,21):
    s+=a/b
    t=a
    a=a+b
    b=t
print(s)


# example 2:
a=2.0
b=1.0
s=0.0

for n in range(1,21):
    s+=a/b
    b,a=a,a+b
print(s)

# 此题目的为求和，中间步骤依次赋值并覆盖，应当比迭代的方法节省资源。


# example 3:

# a=2.0
# b=1.0
# l=[]

# l.append(a/b)
# for n in range(1,20):
#     b,a=a,a+b
#     l.append(a/b)
# print(reduce(lambda x,y:x+y,l))

# Error: reduce is no defined
