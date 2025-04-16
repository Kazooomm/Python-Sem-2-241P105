def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        print("Error, Not divisible by zero")
        return None
    else:
        return float(x / y)

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Enter choice (1/2/3/4): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == '1':
        print(f"The result is: {add(num1, num2)}")
    elif choice == '2':
        print(f"The result is: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"The result is: {multiply(num1, num2)}")
    elif choice == '4':
        result = divide(num1, num2)
        if result is not None:
            print(f"The result is: {result}")
    else:
        print("Invalid input!")

T = True
while T:
    calculator()
    i = input("Do you wish to continue? Y/N : ")
    if i == 'Y' or i == 'y':
        T = True
    else:
        T = False
