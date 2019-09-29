str = "RosMachINEleaRnIGN"
words = str.split()
lower = []
upper = []
for char in str:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)
sorted = ''.join(lower + upper)
print("\n arranging characters giving precedence to lowercase letters:")
print(sorted)
