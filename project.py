VERY_WEAK = 0
WEAK = 1
STRONG = 2
VERY_STRONG = 3

def main():

    print("\n==== Password Strength Test ====")

    while True:
        print("\nChoose from the following options:")
        print("1. Test preset passwords")
        print("2. Test custom password")
        print("3. Exit")
        choice = input("\nEnter your choice: ")

        if choice == '1':
            test_preset_passwords()
        elif choice == '2':
            password = input("Password: ")
            test_custom_password(password)
        elif choice == '3':
            break
        else:
            print("\nWARNING: Invalid option, choose between option 1, 2, or 3")

def test_preset_passwords():

    passwords = ["abc", "1847abc1736", "1245HelloWorld1245", "&@658ABcD26485&$"]
    print("\nHere are some example passwords and their strengths: ")

    for password in passwords:
        strength = test_password_strength(password)
        print(f"     Password: {password} | Strength: {get_strength_string(strength)}")

def get_strength_string(strength):
    strength_strings = ["Very Weak", "Weak", "Strong", "Very Strong"]
    return strength_strings[strength]

def test_password_strength(password):

    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in "!@#$%^&*()-_+=" for char in password)

    if length < 8:
        return VERY_WEAK
    elif length < 12:
        return WEAK
    elif has_upper and has_lower and has_digit and has_special:
        return VERY_STRONG
    elif has_upper and has_lower and has_digit:
        return STRONG
    else:
        return WEAK

def test_custom_password(password):

    if password.strip() == "":
        print("Password: ")
        return

    strength = test_password_strength(password)

    if strength == VERY_WEAK:
        print("Your password is very weak.")
    elif strength == WEAK:
        print("Your password is weak.")
    elif strength == STRONG:
        print("Your password is strong.")
    elif strength == VERY_STRONG:
        print("Your password is very strong.")

if __name__ == "__main__":
    main()
