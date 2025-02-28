passsword = input("Please enter your password:")
length_password = len(passsword)
has_digit = any(char.isdigit() for char in passsword)
has_letter = any(char.isalpha() for char in passsword)
if length_password >= 8 and has_digit and has_letter:
    print("Your password is valid")
else:
    print("Your password must contain at least 8 characters, and a mix of letters and numbers")