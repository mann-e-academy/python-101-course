# Calculator 
# Takes a and b from user and does four main operations on them

while True:
    command = input("Enter your desired operation: ")
    
    if command == "q":
        break

    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
    except:
        pass

    if command == "+":
        print("a + b:", a + b)

    if command == "-":
        print("a - b:", a - b)

    if command == "*":
        print("a * b:", a * b)

    if command == "/":
        try:
            print("a / b:", a / b)
        except:
            print("You cannot do that :-)")