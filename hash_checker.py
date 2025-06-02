import hashlib
import argparse

def calculate_hash(file_path, algo="sha256"):
    try:
        h = hashlib.new(algo)
    except ValueError:
        print(f"[!] Unsupported algorithm: {algo}")
        return

    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    print(f"[+] {algo.upper()} Hash: {h.hexdigest()}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="File Hash Checker")
    parser.add_argument("file", help="Path to the file")
    parser.add_argument("--algo", default="sha256", help="Hash algorithm (default: sha256)")
    args = parser.parse_args()
    calculate_hash(args.file, args.algo)
