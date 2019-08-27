#####################################################
#Find the smallest in the list

a = int(input("Enter the number of terms:\t"))
lst = []
while(a):
    lst.append(int(input()))
    a-=1
print("Minimum value",min(lst))

# OUTPUT:
# Enter the number of terms:	5
# 3
# 2
# 8
# 6
# 1
# Minimum value 1
