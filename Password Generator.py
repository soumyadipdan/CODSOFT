# Password Generator

import random

def generate_password(length):
    # Define the character sets (letters, digits, and symbols)
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    special_chars = '!@#$%^&*()'

    # Combine all character sets into one
    all_characters = lowercase + uppercase + digits + special_chars

    # Create an empty list to store the password
    password = []

    # Randomly select characters from the combined set and add them to the password
    for _ in range(length):
        random_char = random.choice(all_characters)
        password.append(random_char)

    # Convert the list of characters into a string
    return ''.join(password)

# Main logic to run the program
while True:
    print("\n--- Simple Password Generator ---")

    try:
        # Ask the user for the desired password length
        length = int(input("Enter the password length (minimum 4): "))

        # Ensure the password length is at least 4
        if length < 4:
            print("Password length must be at least 4. Please try again.")
            continue

        # Generate the password and display it
        password = generate_password(length)
        print(f"Generated Password: {password}")

        # Ask the user if they want to generate another password
        again = input("Do you want to generate another password? (yes/no): ").lower()
        if again != 'yes':
            print("Goodbye! Stay safe with your new password.")
            break

    except ValueError:
        print("Please enter a valid number for the password length.")
