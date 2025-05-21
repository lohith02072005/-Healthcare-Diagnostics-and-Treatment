from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

def secure_store_symptoms(symptoms):
    encrypted = cipher_suite.encrypt(symptoms.encode())
    decrypted = cipher_suite.decrypt(encrypted).decode()
    return encrypted, decrypted
