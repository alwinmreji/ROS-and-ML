import re

strn = " Math = 98 Science = 99 English = 78 History = 56"
lst = [int(num) for num in re.findall(r'\b\d+\b', strn)]
total = 0
for mark in lst:
  total+=mark

percentage = total/len(lst)  
print("Total Marks is:", total, "Percentage is ", percentage)

#OUTPUT
#
#Total Marks is: 331 Percentage is  82.75
