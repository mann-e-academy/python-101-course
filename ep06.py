# List 

a = [1, 5, 4, 4, 8, 12, 9]
# print(len(a)) # 0 .. len(a) - 1
# print(a[5])

b = [2, 4, 6, 8]
a.extend(b)

# Set

c = set(a)

c = list(c)


# Dictionary 
# Key : Value

d = { "a" : 100, "b" : 2, "c" : 3}
# print(d["a"])

# Tuple 

coord = (10, 20)

## String

text = "Hello, World!"
multiline_text = """Hello, World. 
This is a mutliline text"""

## String splitting

a = "Ali, Muhammad, Reza, Ahmad"
#print(a)

names = a.split(', ')
#print(names)

## Chunking 

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = "This is a string in python."

print(a[:5])
print(a[5:])
print(a[3:7])

print(b[:5])
print(b[5:])
print(b[3:7])
