######################################################
#Split string with user entered value

a = input("Enter a srting:\t")
b = input("Enter the value to split:\t")
c = a.split(b)
s =""
print(c)
for i in c:
    s+=i
    s+=' '
print(s)

#OUTPUT
# Enter a srting:	my_name_is_chotu
# Enter the value to split:	_
# ['my', 'name', 'is', 'chotu']
# my name is chotu
