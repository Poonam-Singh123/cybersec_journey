#!/usr/bin/env python3
"""
Day 5 – Simple Port Scanner
---------------------------
Scans a list of common TCP ports on a given host and
reports which ports are open.
"""

import socket
from datetime import datetime

# A small set of commonly used ports (you can add more if you like)
COMMON_PORTS = {
    21:  "FTP",
    22:  "SSH",
    23:  "Telnet",
    25:  "SMTP",
    53:  "DNS",
    80:  "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306:"MySQL"
}

def scan_port(host: str, port: int) -> bool:
    """Return True if the port is open, False otherwise."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            return s.connect_ex((host, port)) == 0
    except socket.error:
        return False

def main():
    target = input("🔍 Enter target host (domain or IP): ").strip()
    print(f"\n🛡️  Scanning {target}")
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    for port, service in COMMON_PORTS.items():
        if scan_port(target, port):
            print(f"✅ Port {port:<5} ({service:<6}) is OPEN")
        else:
            print(f"❌ Port {port:<5} ({service:<6}) is closed")

    print("\nScan complete ✅")

if __name__ == "__main__":
    main()
