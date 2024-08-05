def password_complexity_checker(password):
    
    length = len(password) >= 9
    uppercase = any(char.isupper() for char in password)
    lowercase = any(char.islower() for char in password)
    digit = any(char.isdigit() for char in password)
    special = any(not char.isalnum() for char in password)

    print(f"Password: {password}")
    print(f"Length (>= 8): {'Pass' if length else 'Fail'}")
    print(f"Uppercase: {'Pass' if uppercase else 'Fail'}")
    print(f"Lowercase: {'Pass' if lowercase else 'Fail'}")
    print(f"Digit: {'Pass' if digit else 'Fail'}")
    print(f"Special Character: {'Pass' if special else 'Fail'}")

    score = sum([length, uppercase, lowercase, digit, special])

    if score == 5:
        print("Password Strength: Very Strong")
    elif score == 4:
        print("Password Strength: Strong")
    elif score == 3:
        print("Password Strength: Medium")
    elif score == 2:
        print("Password Strength: Weak")
    else:
        print("Password Strength: Very Weak")

#Example usage
password = input("Enter a password : ")
password_complexity_checker(password)