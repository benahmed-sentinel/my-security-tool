import hashlib
import time
import os
import socket

# ==============================
# 🔷 TOOL INFO
# ==============================

AUTHOR = "Benahmed Mohamed"
TOOL_NAME = "SentinelRecon"
VERSION = "1.0"

SIGNATURE = "SentinelRecon | Cyber Intelligence Tool"

SECRET_SALT = "9x!QpL@7#Secure"
INVISIBLE_MARK = "\u200b\u200c\u200d"

# ==============================
# 🔐 FINGERPRINT
# ==============================

def generate_fingerprint():
    raw = f"{AUTHOR}{TOOL_NAME}{VERSION}{time.time()}{SECRET_SALT}"
    return hashlib.sha256(raw.encode()).hexdigest()

# ==============================
# 🕵️ TRACKING (LOCAL)
# ==============================

def track_usage(domain):
    try:
        with open(".sentinel_log", "a") as f:
            f.write(f"{domain} | {time.ctime()}\n")
    except:
        pass

# ==============================
# 🌐 BASIC RECON
# ==============================

def resolve_domain(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except:
        return "Failed"

# ==============================
# 🚀 MAIN SCAN
# ==============================

def sentinel_scan(domain):
    print("="*50)
    print(f"{SIGNATURE}")
    print(f"{INVISIBLE_MARK}{AUTHOR}{INVISIBLE_MARK}")
    print("="*50)

    fp = generate_fingerprint()
    print(f"[ID] {fp[:16]}")
    print(f"[Target] {domain}")

    ip = resolve_domain(domain)
    print(f"[IP] {ip}")

    track_usage(domain)

    print("="*50)
    print("Scan Complete ✅")

# ==============================
# ▶️ RUN
# ==============================

if __name__ == "__main__":
    target = input("Enter domain: ")
    sentinel_scan(target)
