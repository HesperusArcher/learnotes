# -*- coding: utf-8 -*-

# via: http://www.runoob.com/python/python-exercise-example4.html

# 题目：输入某年某月某日，判断这一天是这一年的第几天？

# 程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天

# year = int(raw_input('year:\n'))
# month = int(raw_input('month:\n'))
# day = int(raw_input('day:\n'))

    # year=1989
    # month=7
    # day=7

# 改变默认值，封装为函数nday
def nday(year,month,day):

    days=[31,28,31,30,31,30,31,31,30,31,30,31]
    months=[]
    j=0
    for i in range(len(days)):
        months.append(j)
        j+=days[i]

    if 0<month<=12:
        sum=months[month-1]
    else:
        print("date error")

    sum+=day

    leap=0
    if (year%400 ==0) or ((year%4==0) and (year%100 != 0)):
        leap=1
    if (leap==1) and (month>2):
        sum+=1

    # 天数数值转换为字符串，判断最后一位是否为first, second, third
    strsum=str(sum)

    if (strsum[-1]=="1"):
        print('It\'s the',sum,'\bst day.')
    elif (strsum[-1]=="2"):
        print('It\'s the',sum,'\bnd day.')
    elif (strsum[-1]=="3"):
        print('It\'s the',sum,'\brd day.')
    else:
        print('It\'s the',sum,'\bth day.')


nday(1989,7,7)
nday(1990,2,26)
