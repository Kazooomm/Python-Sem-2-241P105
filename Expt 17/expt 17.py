import re

with open("data.txt", "r") as file:
    content = file.read()

# Corrected regular expressions
emails = re.findall(r'\b[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}\b', content)  # Fixed: single backslashes
phones = re.findall(r'\b\d{3}-\d{3}-\d{4}\b', content)  # Matches: 123-456-7890
dates = re.findall(r'\b\d{2}[/-]\d{2}[/-]\d{4}\b', content)  # Matches both / and - separators

print("Emails:", emails)
print("Phone Numbers:", phones)
print("Dates:", dates)

