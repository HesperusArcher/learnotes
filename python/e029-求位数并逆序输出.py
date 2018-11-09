# 题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

# 程序分析：学会分解出每一位数。

x=int(18119)
y=int(1109)
z=int(2018)

def output_number_of_digits(n):
    a=int(n/10000)
    b=int(n%10000/1000)
    c=int(n%1000/100)
    d=int(n%100/10)
    e=int(n%10)
    if a!=0:
        # 此处输出 %s %d 均可
        print("5D:%s%s%d%s%d"%(e,d,c,b,a))
    elif b!=0:
        print("4D:",e,d,c,b)
    elif c!=0:
        print("3D:",e,d,c)
    elif d!=0:
        print("2D:",e,d)
    else:
        print("1D:",e)

output_number_of_digits(x)
output_number_of_digits(y)
output_number_of_digits(z)
