## insertion sort

arr=[3,5,9,8,1]
for i in range(1,len(arr)):
    temp=arr[i]
    j=i-1
    while(j>=0 and temp<arr[j]):
        arr[j+1]=arr[j]
        j=j-1
    arr[j+1]=temp
print(arr)
