#!/usr/bin/env python3
"""
Day 1 – Linux Command Cheatsheet Viewer
---------------------------------------
Run this script to see a list of essential Linux commands,
or type a keyword to filter commands.

Requires: colorama (pip install colorama)
"""

from colorama import init, Fore, Style
init(autoreset=True)

commands = {
    "pwd":    "Print current working directory",
    "ls":     "List files and folders",
    "cd":     "Change directory",
    "mkdir":  "Create a new directory",
    "touch":  "Create an empty file",
    "cat":    "View file contents",
    "rm":     "Remove a file",
    "rmdir":  "Remove an empty directory",
    "chmod":  "Change file permissions",
    "chown":  "Change file owner and group",
    "history":"Show command history",
    "clear":  "Clear the terminal screen",
    "man":    "Display manual page for a command"
}

def show_header():
    print(Fore.CYAN + "\n🛡️  Day 1 – Linux Command Cheatsheet")
    print(Fore.CYAN + "------------------------------------\n")

def display_commands(filter_word=None):
    for cmd, desc in commands.items():
        if not filter_word or filter_word.lower() in cmd.lower() or filter_word.lower() in desc.lower():
            print(f"{Fore.GREEN}{cmd:<10}{Style.RESET_ALL} : {desc}")
    print()

if __name__ == "__main__":
    show_header()
    print("Tip: Type a keyword to filter (or just press Enter to see all)\n")
    keyword = input(Fore.YELLOW + "🔍 Search keyword: " + Style.RESET_ALL).strip()
    display_commands(keyword if keyword else None)
    print(Fore.MAGENTA + "✅ Pro Tip: Combine commands with '&&' to run multiple commands in sequence!\n")
