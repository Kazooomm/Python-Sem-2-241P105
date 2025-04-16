'''
Mohd Qazim Ansari
Fe-D
241P105/36
'''

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num2 == 0:
    print("Division and modulus operations cannot be performed with a divisor of zero.")
else:
    print(f"Addition:       {num1} + {num2} = {num1 + num2}")
    print(f"Subtraction:    {num1} - {num2} = {num1 - num2}")
    print(f"Multiplication: {num1} * {num2} = {num1 * num2}")
    print(f"Division:       {num1} / {num2} = {num1 / num2}")
    print(f"Modulus:        {num1} % {num2} = {num1 % num2}")

