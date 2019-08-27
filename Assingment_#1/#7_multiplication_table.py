#######################################################
#Multiplication table upto user entred value

a,b = int(input("Enter the number:\t")),int(input("Enter the number upto:\t"))
print(*[str(a)+" x "+str(i)+" = "+str(i*a) for i in range(1,b+1)],sep="\n")

#OUPUT:
# Enter the number:	7
# Enter the number upto:	15
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70
# 7 x 11 = 77
# 7 x 12 = 84
# 7 x 13 = 91
# 7 x 14 = 98
# 7 x 15 = 105
