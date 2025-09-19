#!/usr/bin/env python3
"""
Day 8 – Simple Port Scanner
---------------------------
Scans a list of common ports on a given host and reports which are open.

⚠️ Use this only on systems you own or have permission to test.
"""

import socket
from concurrent.futures import ThreadPoolExecutor

# Common ports to scan (you can add more)
COMMON_PORTS = {
    22:  "SSH",
    80:  "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP-Alt"
}

def scan_port(host: str, port: int) -> None:
    """Try to connect to a single port and print result if open."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)  # 1 second timeout
        try:
            s.connect((host, port))
            print(f"✅ {port} ({COMMON_PORTS.get(port, 'Unknown')}) is OPEN")
        except (socket.timeout, ConnectionRefusedError):
            pass  # closed or filtered

if __name__ == "__main__":
    target = input("🔎 Enter host to scan (e.g. example.com or 127.0.0.1): ").strip()

    print(f"\nScanning {target}...\n")
    with ThreadPoolExecutor(max_workers=20) as executor:
        for p in COMMON_PORTS:
            executor.submit(scan_port, target, p)

    print("\n🔍 Scan complete.")
