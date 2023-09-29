import random
import string

def generate_password(length=14):
    # Define the character sets for the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate a random password by selecting characters randomly from the combined set
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

# Example usage:
if __name__ == "__main__":
    password = generate_password()
    print("Generated Password:", password)
