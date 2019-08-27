########################################################
#Factorial of a number

a = int(input("Enter the decimal number:\t"))
mul = 1
for i in range(1,a+1):
    mul*= i
print("Factorial of ",a,"is",mul)

#OUTPUT:
# Enter the decimal number:	5
# Factorial of  5 is 120
