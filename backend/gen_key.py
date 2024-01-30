import secrets

# Specify the desired key length in bytes (e.g., 32 bytes for a 256-bit key)
key_length_bytes = 32

# Generate a random secret key
secret_key = secrets.token_hex(key_length_bytes)

print("Generated Secret Key:", secret_key)
