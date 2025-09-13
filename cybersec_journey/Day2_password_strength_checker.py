#!/usr/bin/env python3
"""
Day 2 – Password Strength Checker
---------------------------------
Checks how strong a password is based on length
and variety of characters.
"""

import re

def check_strength(password: str) -> str:
    score = 0

    # +1 if length is at least 8
    if len(password) >= 8:
        score += 1
    # +1 if contains both lower and upper case
    if re.search(r'[a-z]', password) and re.search(r'[A-Z]', password):
        score += 1
    # +1 if contains digits
    if re.search(r'\d', password):
        score += 1
    # +1 if contains special characters
    if re.search(r'[^A-Za-z0-9]', password):
        score += 1

    if score == 4:
        return "💪 Strong"
    elif score == 3:
        return "🙂 Medium"
    else:
        return "⚠️ Weak"

if __name__ == "__main__":
    pwd = input("🔑 Enter a password to check: ")
    result = check_strength(pwd)
    print(f"Password strength: {result}")
