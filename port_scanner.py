import socket
import argparse

def scan_ports(target, ports):
    print(f"[+] Scanning {target}...")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        sock.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple TCP Port Scanner")
    parser.add_argument("target", help="Target IP or hostname")
    parser.add_argument("--ports", nargs="+", type=int, default=[21,22,23,80,443,3389],
                        help="Ports to scan (default common ports)")
    args = parser.parse_args()
    scan_ports(args.target, args.ports)
