arr=[2,1,11,6,3,10,8]
n=len(arr)
print("Original array : ",arr)
print("Length of an array : ",n)
print("Sorted using built-in function : ",sorted(arr))
def selectionsort(arr):
    for i in range(0,n):
        min=i
        for j in range(min+1,n):
            if(arr[min]>arr[j]):
                min=j
        arr[min],arr[i]=arr[i],arr[min]
    return arr
res=selectionsort(arr)
print("Sorted using selection sort",res)

def insertionsort(arr):
    for i in range(1,n):
        cur=arr[i]
        j=i-1
        while(j>=0 and cur<arr[j]):
            arr[j],arr[j+1]=arr[j+1],arr[j]
            j=j-1
        arr[j+1]=cur
    return arr

res2=insertionsort(arr)
print("Sorted using insertion sort :",res2)



            