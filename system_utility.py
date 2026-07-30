import hashlib
import os
import subprocess


def run_ping_diagnostics(target_ip: str):
    command = f"ping -c 4 {target_ip}"
    subprocess.call(command, shell=True)


def hash_password(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()


def fetch_log_file(filename: str):
    filepath = os.path.join("/var/log/app/", filename)

    with open(filepath, "r") as f:
        return f.read()
