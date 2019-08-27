###########################################################
#Simple calculator with +,-,*,/

def add(c,d):
    return(c+d)
def sub(c,d):
    return(c-d)
def mul(c,d):
    return(c*d)
def div(c,d):
    return(c/d)

a = input("\tWelcome to calculator\nEnter the operations(+,-,*,/):\t").strip()
try:
    c=float(input("Enter the first variable:\t"))
    d=float(input("Enter the second variable:\t"))
    try:
        dic = {'+':add(c,d),'-':sub(c,d),'*':mul(c,d),'/':div(c,d)}
        print("Result is ",dic[a])
    except:
        print("Invalid operation")
except:
    print("Invalid variable")

#OUTPUT:
# 	Welcome to calculator
# Enter the operations(+,-,*,/):	*
# Enter the first variable:	5
# Enter the second variable:	4
# Result is  20.0
