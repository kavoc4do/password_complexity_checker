import string
import getpass

def check_pass():
    password = getpass.getpass("Enter your password: ")

    if len(password) < 14:
        print("Password too weak. It must be at least 14 characters long.")
        return

    strength = 0
    remarks = ''
    lower_count = upper_count = num_count = whitespace_count = special_count = 0

    for char in password:
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            whitespace_count += 1
        else:
            special_count += 1

    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if whitespace_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1

    if strength == 1:
        remarks = 'Password too weak. Change it to make it strong.'
    elif strength == 2:
        remarks = 'Weak password. Change it to a stronger one.'
    elif strength == 3:
        remarks = 'Medium strength. Can be better.'
    elif strength == 4:
        remarks = 'Strong password. Needs to be little more strong.'
    elif strength == 5:
        remarks = 'Strong password. Good enough.'

    print('Your password has:')
    print(f"{lower_count} lowercase letters")
    print(f"{upper_count} uppercase letters")
    print(f"{num_count} digits")
    print(f"{whitespace_count} whitespaces")
    print(f"{special_count} special characters")
    print(f"Password strength: {strength}")
    print(f"Hint: {remarks}")

def ask_for_another_pass():
    while True:
        choice = input('Do you want to enter another password? (y/n): ')
        if choice.lower() == 'y':
            return True
        elif choice.lower() == 'n':
            return False
        else:
            print('Invalid input. Please enter "y" or "n".')

if __name__ == '__main__':
    print("+++ Welcome to the password complexity checker! :) +++")
    while True:
        check_pass()
        if not ask_for_another_pass():
            break


        
    
