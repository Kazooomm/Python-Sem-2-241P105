'''
Mohd Qazim Ansari
Fe-D
241P105/36
'''

# Function to check even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Main program
def main():
    try:
        # Input: Number of values to check
        count = int(input("Enter how many numbers you want to check: "))

        # Loop through each number
        for i in range(count):
            num = int(input(f"Enter number {i + 1}: "))
            result = check_even_odd(num)
            print(f"{num} is {result}.")

    except ValueError:
        print("Invalid input. Please enter valid integers.")

# Run the program
main()

