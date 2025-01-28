import hashlib

# Input data
data = "Hello, World!"

# Create a SHA-3 256 hash object
hash_object = hashlib.sha3_256()

# Update the hash object with the data (must be in bytes)
hash_object.update(data.encode('utf-8'))

# Get the hexadecimal representation of the hash
hash_hex = hash_object.hexdigest()

print("SHA-3 256-bit hash:", hash_hex)
