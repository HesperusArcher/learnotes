def binary_search(list,item):
    low=0
    high=len(list)-1

    while low<=high:
        mid = int((low+high)/2)
        guess=list[mid]
        if guess==item:
            return mid
        elif guess>item:
            high=mid-1
        else:
            low=mid+1
    return None

my_list=[1,3,5,7,9,11,13,15,17,19]

print(binary_search(my_list,7))
print(binary_search(my_list,-1))

# recite version

def bi_se(list,item):
    low=0
    high=len(list)-1

    while low<=high:
        mid=int((low+high)/2)
        # print(mid)
        guess=list[mid]
        if guess==item:
            return mid
        elif guess<item:
            low=mid+1
        else:
            high=mid-1
    return None

my_list=[1,3,5,7,9]

print(bi_se(my_list,7))
