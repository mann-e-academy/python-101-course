# Working with files

# Reading from files

f = open('lorem.txt', 'r') # Reading
content = f.read() # f.readlines()


# A bit of data manipulation.

texts = content.split('.')
# print(texts)

# Writing on files

new_file = open('new_lorem.txt', 'w')

for line in texts:
    new_file.write(line + "\n")

new_file.close()