#!/usr/bin/env python3
"""
Day 4 – File Hash Generator
---------------------------
Calculate the MD5, SHA1 and SHA256 hashes of any file.
Useful for checking file integrity or detecting tampering.
"""

import hashlib
import os

def hash_file(file_path: str):
    if not os.path.isfile(file_path):
        print("❌ File not found.")
        return

    # Choose hashing algorithms
    algorithms = ["md5", "sha1", "sha256"]

    print(f"\n📁 File: {file_path}\n")
    for algo in algorithms:
        h = hashlib.new(algo)
        with open(file_path, "rb") as f:
            # Read in chunks so large files won’t exhaust memory
            for chunk in iter(lambda: f.read(4096), b""):
                h.update(chunk)
        print(f"{algo.upper():<7} : {h.hexdigest()}")
    print("\n✅ Hash generation complete.\n")

if __name__ == "__main__":
    file_name = input("🔍 Enter the path to the file: ").strip()
    hash_file(file_name)
