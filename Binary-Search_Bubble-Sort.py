num=int(input("Enter How many elements : "))
arr=[]
for i in range(1,num+1):
    a=int(input(f"Enter element {i} : "))
    arr.append(a)
n=len(arr)-1

def bubblesort(arr):
    for i in range(0,n):
        for j in range(0,n):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

def binarysearch(arr,target):
    left=0
    right=n
    while(left<=right):
        mid=(left+right)//2
        if(arr[mid]==target):
            return mid
        elif(arr[mid]>target):
            left=mid+1
        else:
            right=mid-1
    return -1
sorted_arr=bubblesort(arr)
print("After Sorting : ",sorted_arr)
target=int(input("Enter a element to search : "))
result=binarysearch(sorted_arr,target)

if result != -1:
    print(f"The Value {target} is found at Position {result}")
else:
    print(f"the value {target} is not found")
        

