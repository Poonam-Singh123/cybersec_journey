#!/usr/bin/env python3
"""
Day 10 – WHOIS Lookup Tool
--------------------------
Fetches WHOIS domain registration details.
Requires: python-whois package
    pip install python-whois
"""

import sys

try:
    import whois
except ImportError:
    print("❌ python-whois is not installed. Install it with:")
    print("   pip install python-whois")
    sys.exit(1)

def get_whois_info(domain: str):
    try:
        w = whois.whois(domain)
        print("\n🌐 WHOIS Information")
        print("-" * 40)
        for key, value in w.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"⚠️ Error fetching WHOIS info: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python Day10_whois_lookup.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]
    get_whois_info(domain)
