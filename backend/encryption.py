from cryptography.fernet import Fernet

# Generate key
key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_message(message):
    encrypted = cipher.encrypt(message.encode())
    return encrypted.decode()

def decrypt_message(encrypted_text):
    decrypted = cipher.decrypt(encrypted_text.encode())
    return decrypted.decode()
