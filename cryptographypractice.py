from cryptography.fernet import Fernet

# Function to generate a unique encryption key for a user
def generate_key():
    return Fernet.generate_key()

# Function to encrypt a message
def encrypt_message(message, key):
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message

# Function to decrypt a message
def decrypt_message(encrypted_message, key):
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    return decrypted_message

# Prompt users for their names and generate encryption keys
user1_name = input("User 1, enter your name: ")
user2_name = input("User 2, enter your name: ")

user1_key = generate_key()
user2_key = generate_key()

print(f"{user1_name}'s key: {user1_key}")
print(f"{user2_name}'s key: {user2_key}")

#main while loop
while True:
    sender = input(f"Enter the sender's name ({user1_name}/{user2_name}): ")
    message = input("Enter your message: ")

    if sender == user1_name:
        encrypted_message = encrypt_message(message, user2_key)
        print(f"Encrypted Message (to {user2_name}): {encrypted_message}")
    elif sender == user2_name:
        encrypted_message = encrypt_message(message, user1_key)
        print(f"Encrypted Message (to {user1_name}): {encrypted_message}")
    else:
        print("Invalid sender name. Please enter a valid name.")

    recipient = input("Enter the recipient's name (type 'q' to quit): ")

    if recipient == 'q':
        break
    elif recipient == user1_name:
        decrypted_message = decrypt_message(encrypted_message, user1_key)
        print(f"{user1_name} received a message: {decrypted_message}")
    elif recipient == user2_name:
        decrypted_message = decrypt_message(encrypted_message, user2_key)
        print(f"{user2_name} received a message: {decrypted_message}")
    else:
        print("Invalid recipient name. Please enter a valid name.")
