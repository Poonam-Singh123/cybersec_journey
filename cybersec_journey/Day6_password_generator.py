#!/usr/bin/env python3
"""
Day 6 – Random Password Generator
---------------------------------
Generates a secure random password with a mix of:
• Upper & lower case letters
• Digits
• Special characters
"""

import secrets
import string

def generate_password(length: int = 12) -> str:
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")
    # Character set: letters + digits + punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    # Use secrets.choice for cryptographically strong randomness
    return ''.join(secrets.choice(characters) for _ in range(length))

if __name__ == "__main__":
    try:
        user_len = input("🔢 Desired password length (default 12): ").strip()
        length = int(user_len) if user_len else 12
        pwd = generate_password(length)
        print(f"\n🔑 Your secure password:\n{pwd}\n")
    except ValueError as e:
        print(f"❌ Error: {e}")
