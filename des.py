from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import os

# Key size for DES must be 8 bytes
key = b'8bytekey'  # Example key (must be exactly 8 bytes)

# Function to encrypt data
def encrypt_data(data, key):
    cipher = DES.new(key, DES.MODE_ECB)  # Using ECB mode
    padded_data = pad(data.encode('utf-8'), DES.block_size)  # Pad data to block size
    encrypted_data = cipher.encrypt(padded_data)
    return encrypted_data

# Function to decrypt data
def decrypt_data(encrypted_data, key):
    cipher = DES.new(key, DES.MODE_ECB)  # Using the same mode as encryption
    decrypted_padded_data = cipher.decrypt(encrypted_data)
    decrypted_data = unpad(decrypted_padded_data, DES.block_size)  # Remove padding
    return decrypted_data.decode('utf-8')

# Example usage
if __name__ == "__main__":
    original_data = "Hello, DES encryption!"
    print(f"Original Data: {original_data}")

    # Encrypt the data
    encrypted = encrypt_data(original_data, key)
    print(f"Encrypted Data: {encrypted.hex()}")  # Hex-encoded output for readability

    # Decrypt the data
    decrypted = decrypt_data(encrypted, key)
    print(f"Decrypted Data: {decrypted}")
