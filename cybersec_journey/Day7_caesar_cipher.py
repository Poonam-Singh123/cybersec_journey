#!/usr/bin/env python3
"""
Day 7 – Caesar Cipher Encoder/Decoder
-------------------------------------
Encrypt or decrypt a message by shifting letters by a key value.
"""

import string

alphabet = string.ascii_lowercase

def caesar(text: str, shift: int, mode: str) -> str:
    """
    Encrypt or decrypt the text using a Caesar cipher.
    mode = 'encode' or 'decode'
    """
    if mode == 'decode':
        shift = -shift
    result = []

    for char in text:
        if char.lower() in alphabet:
            idx = alphabet.index(char.lower())
            new_idx = (idx + shift) % 26
            new_char = alphabet[new_idx]
            # keep original case
            result.append(new_char.upper() if char.isupper() else new_char)
        else:
            result.append(char)  # non-letters stay the same
    return ''.join(result)

if __name__ == "__main__":
    mode = input("🔐 Type 'encode' to encrypt or 'decode' to decrypt: ").strip().lower()
    if mode not in ("encode", "decode"):
        print("❌ Invalid choice. Use 'encode' or 'decode'.")
        exit()

    message = input("💬 Enter your message: ")
    try:
        shift = int(input("➡️  Enter shift key (e.g. 3): "))
    except ValueError:
        print("❌ Shift key must be a number.")
        exit()

    output = caesar(message, shift, mode)
    print(f"\n✅ Result: {output}\n")
