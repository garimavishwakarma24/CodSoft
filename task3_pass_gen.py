# Importing libraries
import random  # for generating random numbers
import string  # for getting all letters and digits

# Function to generate password
def generate_password(length):
    # Defining all characters (letters, digits, punctuation)
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Initializing empty password
    password = ""
    
    # Looping through the length to generate password
    for i in range(length):
        # Adding random character to password
        password += random.choice(all_characters)
    
    # Returning generated password
    return password

# Main function
def main():
    # Getting password length from user
    while True:
        # Asking user for password length
        length = input("Enter password length (minimum 6): ")
        
        # Checking if input is a number
        if length.isdigit():
            length = int(length)
            # Checking if length is less than 8
            if length < 6:
                # Printing error message
                print("Password length should be at least 6.")
            else:
                # Breaking loop if length is valid
                break
        else:
            # Printing error message for invalid input
            print("Invalid input. Please enter a number.")

    # Generating password
    password = generate_password(length)
    
    # Printing generated password
    print("Generated Password: ", password)

# Running main function
if __name__ == "__main__":
    main()
