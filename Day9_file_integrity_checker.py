#!/usr/bin/env python3
"""
Day 9 – File Integrity Checker
------------------------------
Generates and verifies a cryptographic hash of a file to check
if it has been modified.

Usage:
1️⃣ Generate hash for a file
2️⃣ Later, verify the file with the saved hash
"""

import hashlib
import sys
import os

def calculate_hash(filepath: str, algo: str = "sha256") -> str:
    """Calculate hash of the file using the given algorithm."""
    if algo not in hashlib.algorithms_available:
        raise ValueError("Unsupported hash algorithm.")
    h = hashlib.new(algo)
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()

def save_hash(filepath: str, hash_value: str):
    """Save hash to a .hash file."""
    with open(filepath + ".hash", "w") as f:
        f.write(hash_value)

def verify_hash(filepath: str, algo: str = "sha256") -> bool:
    """Compare current hash with saved hash."""
    hash_file = filepath + ".hash"
    if not os.path.exists(hash_file):
        print("❌ Hash file not found. Please generate hash first.")
        return False
    with open(hash_file, "r") as f:
        saved_hash = f.read().strip()
    current_hash = calculate_hash(filepath, algo)
    return saved_hash == current_hash

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python Day9_file_integrity_checker.py generate <file_path>")
        print("  python Day9_file_integrity_checker.py verify <file_path>")
        sys.exit(1)

    action, file_path = sys.argv[1], sys.argv[2]
    if not os.path.isfile(file_path):
        print("❌ File not found.")
        sys.exit(1)

    if action == "generate":
        hash_value = calculate_hash(file_path)
        save_hash(file_path, hash_value)
        print(f"✅ Hash generated & saved: {hash_value}")
    elif action == "verify":
        if verify_hash(file_path):
            print("✅ File integrity OK – no changes detected.")
        else:
            print("⚠️ File integrity check FAILED – file may have been altered!")
    else:
        print("❌ Invalid action. Use 'generate' or 'verify'.")
