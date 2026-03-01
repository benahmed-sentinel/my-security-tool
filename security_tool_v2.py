import socket

def check_domain(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"[+] IP Address: {ip}")
    except:
        print("[-] Domain not found")

def main():
    domain = input("Enter domain (example: google.com): ")
    check_domain(domain)

if __name__ == "__main__":
    main()
