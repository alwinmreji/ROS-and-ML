def find(str):
  words = str.split()
  ch = 0
  digit = 0
  symb = 0
  for char in str:
    if char.islower() or char.isupper():
      ch+=1
    elif char.isnumeric():
      digit+=1
    else:
      symb+=1
  print("char: ",ch,"\ndigit: ",digit,"\nsymbols: ",symb)
str = input("Enter your string\t")
find(str)
