# A program to calculate body mass index 
# Gets height (centimeters)
# Gets weight (kilogram)
# Calculates BMI
# Tells us we're healthy or not (underweight, healthy, overweight, obese)

# BMI Formula : weight(kilogram)/height(m) ** 2 

def convert_height(height):
    """Takes height in centimeters and converts it to meters"""
    return height / 100

def calculate_bmi(weight, height):
    return weight / height ** 2

def greet(name):
    print("Hello,", name)

name = input("Enter your name: ")
weight = input("Enter your weight (in kg): ")
height = input("Enter your height (in cm): ")

weight = float(weight)
height = float(height)

if weight <= 0:
    print("Weight can't be zero or negative.")

if height <= 0:
    print("Height can't be zero or negative.")

height = convert_height(height)
greet(name)
bmi = calculate_bmi(weight, height)

if bmi < 18.5:
    print("You're underweight")
elif 18.5 < bmi < 24.9:
    print("You're healthy")
elif 25 < bmi < 29.9:
    print("You're overweight")
else:
    print("You're obese")
