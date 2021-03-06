# 题目：对10个数进行排序。

# 程序分析：可以利用选择法，即从后9个比较过程中，选择一个最小的与第一个元素交换，下次类推，即用第二个元素与后8个进行比较，并进行交换。

if __name__ == "__main__":
    N=10
    l=[2,7,3,9,5,8,6,1,17,13]
    print(l)

    for i in range(N-1):
        min=i
        for j in range(i+1,N):
            if l[min]>l[j]:
                min=j
        l[i],l[min]=l[min],l[i]
    print(l)
