import re
# Regex patterns
phone_pattern = re.compile(r'^\+?[0-9]{10,15}$')  # Valid: +1234567890 or 1234567890
email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$')  # Valid: user@example.com

# Input from user
phone = input("Enter your phone number (with or without country code): ")
email = input("Enter your email ID: ")

# Validate phone
if phone_pattern.match(phone):
    print('☑ Phone number is valid.')
else:
    print('✗ Invalid phone number format.')

# Validate email
if email_pattern.match(email):
    print('☑ Email ID is valid.')
else:
    print('✗ Invalid email ID format.')
