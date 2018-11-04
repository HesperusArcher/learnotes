# -*- coding: utf-8 -*-

# 题目：输出 9*9 乘法口诀表。

# 程序分析：分行与列考虑，共9行9列，i控制行，j控制列。

for i in range(1,10):
    print()
    for j in range(1,i+1):
        # 使用end= 参数使得结果不会非恰当地断行，需要配合前一项"\t"，尚不知具体原因
        print(i,"*",j,"=",i*j,"\t",end="\b")
        # 此二句结果相同
        # print("%d * %d = %d \t" % (i,j,i*j),end="\b")
