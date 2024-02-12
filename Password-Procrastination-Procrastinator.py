import random
import string

def generate_password(length=8, use_uppercase=True, use_digits=True, use_special_chars=True):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        print("Welcome to the Password Generator!")
        length = int(input("Enter the length of the password: "))
        use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == "yes"
        use_digits = input("Include digits? (yes/no): ").lower() == "yes"
        use_special_chars = input("Include special characters? (yes/no): ").lower() == "yes"
     
        password = generate_password(length, use_uppercase, use_digits, use_special_chars)
        print("Your generated password is:", password)
    except ValueError:
        print("Invalid Value!!! Type in only integer and string")

if __name__ == "__main__":
    main()