import os
import platform
import pyfiglet
from colorama import Fore, Style

# Banner function
def banner():
    ascii_banner = pyfiglet.figlet_format("NetScanner")
    print(Fore.CYAN + ascii_banner + Style.RESET_ALL)
    print(Fore.YELLOW + "🔍 Simple Network Scanner for Kali Linux" + Style.RESET_ALL)
    print(Fore.GREEN + "-" * 60 + Style.RESET_ALL)

# Ping function
def ping_host(ip):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = f"ping {param} 1 -W 1 {ip} > /dev/null 2>&1"
    return os.system(command) == 0

# Scan function
def scan_network(base_ip):
    print(f"\n{Fore.BLUE}Scanning {base_ip}.0/24 network...{Style.RESET_ALL}\n")
    for i in range(1, 255):
        ip = f"{base_ip}.{i}"
        if ping_host(ip):
            print(Fore.GREEN + f"[+] Host {ip} is UP" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"[-] Host {ip} is DOWN" + Style.RESET_ALL)

# Main
if __name__ == "__main__":
    banner()
    base_ip = input("Enter base IP (e.g. 192.168.1): ")
    scan_network(base_ip)
