import getpass

# First level authentication
passphrase = getpass.getpass("Enter your passphrase: ")
if passphrase == "myPassphrase":
    print("Level 1 authentication successful.")
else:
    print("Invalid passphrase!")
    exit()

# Second level authentication
print("Select your image:")
print("1. Image 1")
print("2. Image 2")
print("3. Image 3")
image_choice = input("Enter your choice: ")
if image_choice == "2":
    print("Level 2 authentication successful.")
else:
    print("Invalid image!")
    exit()

# Third level authentication
password = getpass.getpass("Enter your password: ")
if password == "myPassword":
    print("Level 3 authentication successful.")
else:
    print("Invalid password!")
    exit()

print("Authentication successful!")