from cryptography.fernet import Fernet
import os


KEY_FILE = "secret.key"


def generate_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()

        with open(KEY_FILE, "wb") as file:
            file.write(key)

        print("Encryption key created.")


def load_key():
    with open(KEY_FILE, "rb") as file:
        return file.read()


def encrypt_file(filename):
    try:
        key = load_key()
        fernet = Fernet(key)

        with open(filename, "rb") as file:
            data = file.read()

        encrypted_data = fernet.encrypt(data)

        encrypted_filename = filename + ".encrypted"

        with open(encrypted_filename, "wb") as file:
            file.write(encrypted_data)

        print("File encrypted successfully!")
        print("Saved as:", encrypted_filename)

    except FileNotFoundError:
        print("File not found.")


def decrypt_file(filename):
    try:
        key = load_key()
        fernet = Fernet(key)

        with open(filename, "rb") as file:
            encrypted_data = file.read()

        decrypted_data = fernet.decrypt(encrypted_data)

        decrypted_filename = filename.replace(
            ".encrypted", "_decrypted"
        )

        with open(decrypted_filename, "wb") as file:
            file.write(decrypted_data)

        print("File decrypted successfully!")
        print("Saved as:", decrypted_filename)

    except FileNotFoundError:
        print("File not found.")

    except Exception:
        print("Decryption failed. Make sure you are using the correct key and encrypted file.")


generate_key()


while True:
    print("\n===== FILE ENCRYPTION TOOL =====")
    print("1. Encrypt File")
    print("2. Decrypt File")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        filename = input("Enter the file name to encrypt: ")
        encrypt_file(filename)

    elif choice == "2":
        filename = input("Enter the encrypted file name: ")
        decrypt_file(filename)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1, 2, or 3.")