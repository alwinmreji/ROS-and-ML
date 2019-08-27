#####################################################
# Selection Sort in Python

def selectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[min] > arr[j]:
                min = j
                arr[i], arr[min] = arr[min], arr[i]

arr=[]
n=int(input("Enter array size:"))
for i in range(0,n):
    ele=int(input())
    arr.append(ele)
selectionSort(arr)
print("Sorted array:")
for i in range(0,n):
    print(arr[i])

#OUTPUT:
# Enter array size:4
# 9
# 3
# 4
# 1
# Sorted array:
# 1
# 4
# 3
# 9
