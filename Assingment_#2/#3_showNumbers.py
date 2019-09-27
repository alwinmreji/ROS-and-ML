def check (i):
  if i%2 == 0:
    return "EVEN"
  else:
    return "ODD"
def showNumbers(limit):
  for i in range(0,limit+1):
    print(i,check(i))

limit = int(input("Enter a limit:\t"))
showNumbers(limit)
# OUTPUT
# Enter a limit:   10
# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD
# 4 EVEN
# 5 ODD
# 6 EVEN
# 7 ODD
# 8 EVEN
# 9 ODD
# 10 EVEN
