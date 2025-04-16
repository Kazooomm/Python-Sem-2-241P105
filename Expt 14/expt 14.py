def Division():
    """Performs division with exception handling."""
    try:
        num1 = float(input("Enter the numerator: "))
        num2 = float(input("Enter the denominator: "))
        result = num1 / num2
    except ValueError:
        print("Error: Invalid input! Please enter numeric values.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"Result: {result}")
    finally:
        print("Execution completed.")

Division()
