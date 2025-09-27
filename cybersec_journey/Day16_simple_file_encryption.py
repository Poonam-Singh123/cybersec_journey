#!/usr/bin/env python3
"""
Day 16 – Simple File Encryption & Decryption
--------------------------------------------
Encrypt and decrypt text files using Fernet (symmetric encryption).
"""

from cryptography.fernet import Fernet
import sys
import os

KEY_FILE = "secret.key"

def generate_key():
    """Generate and save a key if it doesn't exist yet."""
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, 'wb') as key_file:
            key_file.write(key)
        print("✅ Key generated and saved as secret.key")
    else:
        print("🔑 Key already exists (secret.key)")

def load_key():
    """Load the previously generated key."""
    with open(KEY_FILE, 'rb') as key_file:
        return key_file.read()

def encrypt_file(filename):
    """Encrypt the given file."""
    key = load_key()
    fernet = Fernet(key)

    with open(filename, 'rb') as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(filename + ".encrypted", 'wb') as enc_file:
        enc_file.write(encrypted)

    print(f"🔒 Encrypted {filename} → {filename}.encrypted")

def decrypt_file(filename):
    """Decrypt an encrypted file."""
    key = load_key()
    fernet = Fernet(key)

    with open(filename, 'rb') as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    original_name = filename.replace(".encrypted", ".decrypted")
    with open(original_name, 'wb') as dec_file:
        dec_file.write(decrypted)

    print(f"🔓 Decrypted {filename} → {original_name}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python Day16_simple_file_encryption.py genkey")
        print("  python Day16_simple_file_encryption.py encrypt <filename>")
        print("  python Day16_simple_file_encryption.py decrypt <filename>")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "genkey":
        generate_key()
    elif command == "encrypt" and len(sys.argv) == 3:
        encrypt_file(sys.argv[2])
    elif command == "decrypt" and len(sys.argv) == 3:
        decrypt_file(sys.argv[2])
    else:
        print("❗ Invalid usage. See instructions above.")
