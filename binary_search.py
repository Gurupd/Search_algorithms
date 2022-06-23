
def binary_search(arr,target):
    left=0
    right=len(arr)-1
    
    while(left<=right):
        mid=(left+right)//2
        if target==arr[mid]:
            return(mid)
        elif target<arr[mid]:
            right=mid-1
        else:
            left=mid+1



print(binary_search([-5,2,4,6,10],10))
print(binary_search([-5,2,4,6,10],6))
print(binary_search([-5,2,4,6,10],20))
# Time complexity ---O(logn)
