import re

def check_password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*()_+=\-{}\[\]:;\"'<>,.?/\\|]", password):
        score += 1

    print(f"[+] Password strength score: {score}/5")
    if score < 3:
        print("[!] Weak password")
    elif score < 5:
        print("[~] Moderate password")
    else:
        print("[✓] Strong password")

if __name__ == "__main__":
    pwd = input("Enter password to check: ")
    check_password_strength(pwd)
