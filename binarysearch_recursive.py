
def bs_recursive(arr,target):
    return (search(arr,target,0,len(arr)-1))

def search(arr,target,left_index,right_index):
    if (left_index>right_index):
        return -1
    mid=(left_index+right_index)//2
    if target==arr[mid]:
        return(mid)
    elif(target<arr[mid]):
        return(search(arr,target,left_index,mid-1))
    else:
        return(search(arr,target,mid+1,right_index))





print(bs_recursive([-5,2,4,6,10],10))
print(bs_recursive([-5,2,4,6,10],6))
print(bs_recursive([-5,2,4,6,10],20))