#!/usr/bin/env python3
"""
Day 14 – Simple Packet Sniffer
------------------------------
Captures network packets and prints basic info:
• Source & Destination IP
• Protocol type

⚠️ Requires administrative/root privileges.
⚠️ Use only on networks you own or have explicit permission to monitor.

Dependencies:
    pip install scapy
"""

from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = "OTHER"
        if TCP in packet:
            proto = "TCP"
        elif UDP in packet:
            proto = "UDP"
        print(f"[{proto}] {ip_src} -> {ip_dst}")

if __name__ == "__main__":
    print("🔍 Starting packet capture (Press Ctrl+C to stop)...\n")
    # sniff on default interface, show 10 packets then stop
    sniff(count=10, prn=packet_callback)
    print("\n✅ Capture complete.")
