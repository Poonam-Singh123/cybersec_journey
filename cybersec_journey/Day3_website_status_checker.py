#!/usr/bin/env python3
"""
Day 3 – Website Status Checker
------------------------------
Checks whether a website is reachable and reports the HTTP status code
and response time.
"""

import requests
import time

def check_website(url: str):
    if not url.startswith(("http://", "https://")):
        url = "https://" + url  # assume https if no scheme given
    print(f"\n🌐 Checking {url}")
    start = time.time()
    try:
        response = requests.get(url, timeout=5)
        elapsed = time.time() - start
        print(f"✅ Status code: {response.status_code}")
        print(f"⚡ Response time: {elapsed:.2f} seconds")
    except requests.exceptions.RequestException as e:
        print(f"❌ Could not reach the website.")
        print(f"Error: {e}")

if __name__ == "__main__":
    site = input("🔍 Enter a website (e.g. example.com): ").strip()
    check_website(site)
