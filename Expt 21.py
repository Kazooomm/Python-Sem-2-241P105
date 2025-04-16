
import tkinter as tk
from tkinter import ttk, messagebox

def submit_form():
    name = name_entry.get()
    branch = branch_var.get()
    game = game_entry.get()

    if not name or not branch or not game:
        messagebox.showWarning("Input Error", "Please fill in all fields.")
        return

    output_label.config(text=f"  Submission Successful! \nName: {name} \nBranch: {branch} \nGame: {game}")

# Create main window
root = tk.Tk()
root.title("College Admission Form")
root.geometry("480x300")

# Name Label & Entry
tk.Label(root, text="Name:", font=("Arial", 12)).pack(pady=5)
name_entry = tk.Entry(root, width=30)
name_entry.pack()

# Branch Label & Dropdown
tk.Label(root, text="Branch:", font=("Arial", 12)).pack(pady=5)
branch_var = tk.StringVar()
branches = ["Computer Science", "Electronics", "Mechanical", "Civil", "Electrical"]
branch_dropdown = ttk.Combobox(root, textvariable=branch_var, values=branches, width=28, state="readonly")
branch_dropdown.pack()
branch_dropdown.set("Select Branch")

# Favorite Game Label & Entry
tk.Label(root, text="Favorite Game:", font=("Arial", 12)).pack(pady=5)
game_entry = tk.Entry(root, width=30)
game_entry.pack()

# Submit Button
submit_button = tk.Button(root, text="Submit", font=("Arial", 12, "bold"), command=submit_form)
submit_button.pack(pady=10)

# Output Label
output_label = tk.Label(root, text="", font=("Arial", 12), fg="green")
output_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
