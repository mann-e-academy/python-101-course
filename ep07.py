# Loops 

## While Loop

count = 0

# while count < 100:
#     print(count)
#     count += 1 # count = count + 1

# while count < 100:
#     print(count)
#     count += 1
#     if count == 85:
#         break

## For Loop 

a = [1, 2, 3, 4, 5, 6, 7, 8]

# for i in range(len(a)):
#     print(a[i])

## range() method 

# a = range(5, 10)
# print(a)

## For loop in a list
 
# for i in a:
#     if i % 2 == 0:
#         b.append(i)

# print(b)

## list comprehension

b = [i for i in a if i % 2 == 0]
print(b)