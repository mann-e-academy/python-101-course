# Error Handling in Python

students = { "Ali" : 20, "Ahmad" : 15, "Reza" : 18, "Muhammad" : 15}
name = input("Enter your name: ")

try:
    print(students[name])
except Exception as e:
    print(f"Got exception {e}")
