from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_text(text):
    encrypted = cipher.encrypt(text.encode())
    return encrypted

def decrypt_text(encrypted_text):
    decrypted = cipher.decrypt(encrypted_text).decode()
    return decrypted
