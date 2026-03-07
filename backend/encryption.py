from cryptography.fernet import Fernet

# Generate a valid Fernet key automatically
key = Fernet.generate_key()

fernet = Fernet(key)

def encrypt_text(text):
    encrypted = fernet.encrypt(text.encode())
    return encrypted.decode()

def decrypt_text(text):
    decrypted = fernet.decrypt(text.encode())
    return decrypted.decode()
