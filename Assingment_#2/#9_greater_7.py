def middle(strn):
  index = int(len(strn) /2)
  print("String ", strn)
  mid = strn[index-1:index+2]
  print("Middle", mid)
  
middle("fgi")
middle("ghi")

#OUTPUT
#String  fgi
#Middle fgi
#String  ghi
#Middle ghi
