##########################################################
#Decimal to Binary using recrusion

def binary(a,b):
    b+= str(a%2)
    a//=2
    if a:
        b=binary(a,b) #using recrusion
    return b

a,b  = int(input("Enter the decimal number:\t")),""
print("Binary conversion is:",binary(a,b)[::-1])

#OUTPUT:
#Enter the decimal number:	15
# Binary conversion is: 1111
