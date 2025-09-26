#!/usr/bin/env python3
"""
Day 15 – Password Strength Checker
----------------------------------
Checks the strength of a password based on:
• Length
• Use of uppercase/lowercase letters
• Numbers
• Special characters
and gives a strength rating & tips.
"""

import re

def check_password_strength(password: str) -> tuple[str, list[str]]:
    """
    Returns a rating ("Weak", "Moderate", "Strong") and a list of suggestions.
    """
    suggestions = []
    score = 0

    # Criteria
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 12 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add numbers.")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        suggestions.append("Add special characters (e.g. !@#$%).")

    # Rating
    if score >= 6:
        rating = "Strong"
    elif score >= 4:
        rating = "Moderate"
    else:
        rating = "Weak"

    return rating, suggestions

if __name__ == "__main__":
    pwd = input("🔑 Enter the password to check: ").strip()
    rating, tips = check_password_strength(pwd)

    print(f"\n🔎 Password strength: {rating}")
    if tips:
        print("💡 Suggestions to improve:")
        for t in tips:
            print(f"   - {t}")
    else:
        print("✅ Great! Your password is strong.")
