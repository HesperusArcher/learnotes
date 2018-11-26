# 题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。

# 程序分析：首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。


# 0作为加入数字的占位符
a=[1,4,6,9,13,16,19,28,40,100,0]

print(a)

number=7

end=a[-2]

if number>end:
    a[-1]=number
else:
    for i in range(len(a)-1):
        if a[i]>number:
            temp1=a[i]
            a[i]=number
            for j in range(i+1,len(a)):
                temp2=a[j]
                a[j]=temp1
                temp1=temp2
            break
print(a)

# 因为加入了占位符，故end=a[-n]，range(len(a)-n) 的n值一定要弄清楚。
