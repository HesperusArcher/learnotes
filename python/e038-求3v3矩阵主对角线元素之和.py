# 程序分析：利用双重for循环控制输入二维数组，再将a[i][i]累加后输出。

a=[]
sum=0.0

# for i in range(3):
#     a.append([])
#     for j in range(3):
#         a[i].append(float())

a=[[78,34,23],[34,56,33],[12,21,2]]

for i in range(3):
    for j in range(3):
        if i==j:
            sum+=a[i][j]
print(sum)
