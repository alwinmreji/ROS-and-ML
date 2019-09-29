def append(str1, str2):
  mid = int(len(str1) /2)
  print("Strings are", str1, str2)
  three = str1[:mid-1:]+ str2 +str1[mid-1:]
  print("After appending new string is", three)

append("python", "testing")
