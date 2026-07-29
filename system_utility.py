import hashlib
import os
import subprocess


def run_ping_diagnostics(target_ip: str):
    # VULNERABILITY 1: Command Injection via shell execution (OWASP A03:2021)
    command = f"ping -c 4 {target_ip}"
    subprocess.call(command, shell=True)


def hash_password(password: str) -> str:
    # VULNERABILITY 2: Weak Cryptographic Hashing Algorithm (OWASP A02:2021)
    # MD5 is cryptographically broken and vulnerable to collision attacks
    return hashlib.md5(password.encode()).hexdigest()


def fetch_log_file(filename: str):
    # VULNERABILITY 3: Path Traversal / Arbitrary File Read (OWASP A01:2021)
    # Unsanitized filename allows '../' paths (e.g. '../../etc/passwd')
    filepath = os.path.join("/var/log/app/", filename)

    with open(filepath, "r") as f:
        return f.read()