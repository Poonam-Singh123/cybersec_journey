#!/usr/bin/env python3
"""
Day 13 – File Encryption & Decryption Tool
------------------------------------------
Encrypts and decrypts any file using a password-derived key.

⚠️ For educational use only. Do not use for real confidential data.
Requires:
    pip install cryptography
"""

import sys
import os
import base64
import hashlib
from cryptography.fernet import Fernet

def password_to_key(password: str) -> bytes:
    """
    Derive a 32-byte Fernet key from a password using SHA-256,
    then URL-safe base64 encode it.
    """
    return base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())

def encrypt_file(password: str, filepath: str):
    key = password_to_key(password)
    cipher = Fernet(key)
    with open(filepath, "rb") as f:
        data = f.read()
    encrypted = cipher.encrypt(data)
    with open(filepath + ".enc", "wb") as f:
        f.write(encrypted)
    print(f"✅ Encrypted file saved as: {filepath}.enc")

def decrypt_file(password: str, filepath: str):
    if not filepath.endswith(".enc"):
        print("❌ Encrypted file must end with .enc")
        return
    key = password_to_key(password)
    cipher = Fernet(key)
    with open(filepath, "rb") as f:
        encrypted = f.read()
    try:
        decrypted = cipher.decrypt(encrypted)
    except Exception:
        print("❌ Decryption failed. Wrong password or corrupt file.")
        return
    out_name = filepath[:-4] + ".dec"
    with open(out_name, "wb") as f:
        f.write(decrypted)
    print(f"✅ Decrypted file saved as: {out_name}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage:")
        print("  python Day13_file_encryption_tool.py encrypt <file_path> <password>")
        print("  python Day13_file_encryption_tool.py decrypt <file_path.enc> <password>")
        sys.exit(1)

    action, file_path, password = sys.argv[1], sys.argv[2], sys.argv[3]
    if not os.path.isfile(file_path):
        print("❌ File not found.")
        sys.exit(1)

    if action == "encrypt":
        encrypt_file(password, file_path)
    elif action == "decrypt":
        decrypt_file(password, file_path)
    else:
        print("❌ Invalid action. Use 'encrypt' or 'decrypt'.")
