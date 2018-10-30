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
# filter object at <xxxxxxxx>

# import math
# def func_get_prime(n):
#     return filter(lambda x: not [x%i for i in range(2, int(math.sqrt(x))+1) if x%i == 0], range(2, n+1))
# print(func_get_prime(100))


# method 3:

import math

num=[]
i=2
for i in range(2,100):
    j=2
    # 引入k=math.sqrt(i)，k为i的平方根，即可能的最大公因数
    k=int(math.sqrt(i)+1)
    # > 假如某个数n不是素数，则一定可以分解成x*y形式。
    # > 由此可以推论，n不是素数，则一定可以被某个小于n的数整除。
    # > 而对n来说，最小公因数最大只可能为n的平方根，因为假如存在一个大于n平方根的公因数x，则一定存在另一个公因数y＝n/x, y<x。从上面的推理可以得出结论，如果n不能被所有小于等于它的平方根的整数整除，则n为素数。
    for j in range(2,k):
        if (i%j==0):
            break
    else:
        num.append(i)
print(num)
