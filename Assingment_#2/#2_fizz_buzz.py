def fizz_buzz(n):
  if n%3 == 0:
    if n%5 == 0:
      return "FizzBuzz"
    return "Fizz"
  elif n%5 == 0:
    return "Buzz"
  return n

a = int(input("Enter a number to check:\t"))
print(fizz_buzz(a))

# OUTPUT
# Enter a number to check: 6
# Fizz
# Enter a number to check: 5
# Buzz
# Enter a number to check: 15
# FizzBuzz
