import socket
socket.setdefaulttimeout(1)
count = 0
domain = input("Enter a domain name (example: google.com): ")
try:
    print("1.Small Scan(3-5s)\n" \
    "2. Medium scan(15-30s)\n" \
    "3. Large Scan(1m+)")
    chi=int(input("Enter choice: "))
    match chi:
        case 1:
            try:
                with open("subdomains_small.txt", "r") as f:
                    sub_domains = f.read().splitlines()
            except FileNotFoundError:
                print("subdomains_small.txt file not found.")
        case 2:
            try:
                with open("subdomains_medium.txt", "r") as f:
                    sub_domains = f.read().splitlines()
            except FileNotFoundError:
                print("subdomains_medium.txt file not found.")
        case 3:
            try:
                with open("subdomains_large.txt", "r") as f:
                    sub_domains = f.read().splitlines()
            except FileNotFoundError:
                print("subdomains_large.txt file not found.")
        case _:
            print("Enter a valid value")  
except ValueError:
    print("Error")
print("\nScanning for subdomains...\n")
for sub in sub_domains:
    fulldom = sub + "." + domain
    try:
        ip = socket.gethostbyname(fulldom)
        print("[FOUND]",fulldom," ->" ,ip)
        count += 1
    except socket.gaierror:
        pass
print("\nTotal subdomains found: ", count)
