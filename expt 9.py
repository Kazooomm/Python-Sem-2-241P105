'''
MOHD QAZIM ANSARI
241P105/36
FE-D
27/02/25
'''

n = int(input("enter the number :"))

if n < 0:
    print("factorial is not defined for the negative number")
else:
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(f"factorial of {n} is {result}")

