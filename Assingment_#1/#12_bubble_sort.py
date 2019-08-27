#Bubble sort

def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1] :
                    arr[j], arr[j+1] = arr[j+1], arr[j]
arr=[]
n=int(input("Enter array size:"))
for i in range(0,n):
    ele=int(input())
    arr.append(ele)
bubbleSort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
    print (arr[i])

#OUTPUT:
# Enter array size:5
# 9
# 4
# 5
# 2
# 8
# Sorted array is:
# 2
# 4
# 5
# 8
# 9
