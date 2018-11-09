# 题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

a=int(13531)
x=str(a)
flag=True

for i in range(int(len(x)/2)):
    if x[i] != x[-i-1]:
        flag=False
        break
if flag:
    print("%d is." % a)
else:
    print("%s is not." % x)
