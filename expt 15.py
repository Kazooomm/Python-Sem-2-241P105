import pdb
def divide_numbers(a, b):
    if b == 0:
        return "Error: Division by zero" # Handle division by zero gracefully
        result = a / b
        return result
def calculate_average(numbers):
        numbers = [int(num) if isinstance(num, str) else num for num in numbers]
        # Convert strings to integers
        total = sum(numbers)
        return total / len(numbers)
def main():
        numbers = [10, 20, 30, 40, '50']
        # Intentional error: one of the numbers is a string
        avg = calculate_average(numbers) # This will raise an error due to the string '50'
        print(f"The average is: {avg}")
        a, b = 10, 0 # Intentional division by zero error
        result = divide_numbers(a, b) # This will raise a ZeroDivisionError
        print(f"The result of division is: {result}")
if __name__ == '__main__':
        main()

