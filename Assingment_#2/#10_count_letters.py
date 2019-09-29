a = input("your input: ")
count = 0
for char in a:
  if(char.islower() or char.isupper()):
    count+=1
print("OUTPUT is: ",count)

#OUTPUT
#your input: 89r ew
#OUTPUT is: 3
