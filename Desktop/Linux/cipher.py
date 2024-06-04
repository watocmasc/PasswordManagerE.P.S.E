from cryptography.fernet import Fernet
import os

def write_key():
    key = Fernet.generate_key()
    home_dir = os.path.expanduser("~")

    with open(f"{home_dir}/.config/epse-config/crypto.key", 'wb') as key_file:
        key_file.write(key)

def load_key():
    home_dir = os.path.expanduser("~")
    return open(f"{home_dir}/.config/epse-config/crypto.key", 'rb').read()

def encrypt(filename, key):
    f = Fernet(key)

    with open(filename, 'rb') as file:
        file_data = file.read()

    encrypted_data = f.encrypt(file_data)

    with open(filename, 'wb') as file:
        file.write(encrypted_data)

def decrypt(filename, key):
    f = Fernet(key)

    with open(filename, 'rb') as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)

    with open(filename, 'wb') as file:
        file.write(decrypted_data)