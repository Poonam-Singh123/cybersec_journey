#!/usr/bin/env python3
"""
Day 11 – Basic Log File Analyzer
--------------------------------
Scans a web server log file and:
• Counts total requests
• Highlights HTTP errors (4xx & 5xx)
• Lists the top 5 most frequent IP addresses
"""

from collections import Counter
import re
import sys
import os

# Regex pattern for a typical Apache/Nginx access log line
LOG_PATTERN = re.compile(
    r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3})\s.*"\s(?P<status>\d{3})\s'
)

def analyze_log(log_path: str):
    if not os.path.isfile(log_path):
        print("❌ File not found.")
        return

    total_requests = 0
    error_count = 0
    ip_counter = Counter()

    with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            total_requests += 1
            match = LOG_PATTERN.search(line)
            if match:
                ip = match.group("ip")
                status = int(match.group("status"))
                ip_counter[ip] += 1
                if 400 <= status < 600:
                    error_count += 1

    print("\n📊 Log Analysis Report")
    print("-" * 40)
    print(f"Total requests: {total_requests}")
    print(f"Total errors (4xx/5xx): {error_count}")
    print("\nTop 5 IPs by request count:")
    for ip, count in ip_counter.most_common(5):
        print(f"  {ip} -> {count} requests")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python Day11_log_file_analyzer.py <access_log_file>")
        sys.exit(1)

    analyze_log(sys.argv[1])
