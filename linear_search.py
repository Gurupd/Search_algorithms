
def linear_search(list,target):
    for i in range(0,len(list)-1):
        if list[i]==target:
            return i
    return -1

list=[1,-8,3,9]
target=10
print(linear_search(list,target))