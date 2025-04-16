import tkinter as tk
from tkinter import messagebox
import random

# Function to check the user's guess
def check_guess():
    try:
        user_guess = int(entry.get())  # Get the user's guess from the entry widget
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid number.")
        return

    # Check if the guess is correct
    if user_guess < target_number:
        messagebox.showinfo("Try Again", "Too low! Try again.")
    elif user_guess > target_number:
        messagebox.showinfo("Try Again", "Too high! Try again.")
    else:
        messagebox.showinfo("Congratulations!", "You guessed the correct number!")
        reset_game()  # Reset the game after correct guess

# Function to reset the game
def reset_game():
    global target_number
    target_number = random.randint(1, 100)  # Generate a new random number
    entry.delete(0, tk.END)  # Clear the entry field
    label_result.config(text="Guess a number between 1 and 100")  # Reset the label

# Set up the main window
root = tk.Tk()
root.title("Number Guessing Game")

# Create a label
label_instructions = tk.Label(root, text="Guess a number between 1 and 100:")
label_instructions.pack(pady=10)

# Create an entry widget for the user to input their guess
entry = tk.Entry(root)
entry.pack(pady=10)

# Create a button that calls the check_guess function when clicked
button_check = tk.Button(root, text="Check Guess", command=check_guess)
button_check.pack(pady=10)

# Create a label for result/feedback
label_result = tk.Label(root, text="Guess a number between 1 and 100")
label_result.pack(pady=10)

# Generate a random target number
target_number = random.randint(1, 100)

# Start the GUI event loop
root.mainloop()
