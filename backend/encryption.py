from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_message(message: str):
    encrypted = cipher.encrypt(message.encode())
    return encrypted.decode()

def decrypt_message(token: str):
    decrypted = cipher.decrypt(token.encode())
    return decrypted.decode()
