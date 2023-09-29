# Method (Function)

def print_something():
    print("Something...")

print_something()

def greet(name):
    print("Hello, ", name)

greet("World")

def add(a, b):
    return a + b 

print(add(10, 20))
a = 10 
b = 20
c = add(10, 20)
c = add(a, b)

print(c)

def add(a: int, b: int):
    # type safety
    return a + b 

def greet(name = "World"):
    print("Hello,", name)

greet()
greet("Muhammadreza")

# n -> n - 1 : Recursive Functions

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(1))
print(factorial(5))

def f(x):
    """It calculates x to the power of 2"""
    return(x ** 2)