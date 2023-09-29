# if ... else 

# Getting user input

a = input("Enter value of A: ")
# b = input("Enter value of B: ")

# type casting:

a = int(a)
# b = int(b)

# if a > b:
#     print("a > b")
# elif a == b:
#     print("a equals b")
# else:
#     print("a < b")

# FizzBuzz 
# If A is divisible by 3 print out Fizz
# If A is divisible by 5 print out Buzz
# If A is divisible by 3 and 5 print out FizzBuzz

if a % 15 == 0:
    print("FizzBuzz")
elif a % 5 == 0:
    print("Buzz")
elif a % 3 == 0:
    print("Fizz")
else:
    print("None of it was correct.")