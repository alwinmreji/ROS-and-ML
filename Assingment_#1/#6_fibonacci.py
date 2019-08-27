########################################################
#Fibonacci number count

a = int(input("Enter the decimal number:\t"))
f,s = 1,0
print("The Fibonacci numbers are:\n")
while(a):
    s+=f
    f = s-f
    a-=1
    print(f)

#OUTPUT:
# Enter the decimal number:	10
#The Fibonacci numbers are:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
