import requests
import socket
def web_recon():
    def check_security_headers(response):
        security_headers = [
            "X-Frame-Options",
            "Content-Security-Policy",
            "Strict-Transport-Security",
            "X-Content-Type-Options"
        ]
        result = "\nSecurity Header Analysis:\n"

        for header in security_headers:
            if header in response.headers:
                result+=(f"{header}: Present\n")
            else:
                result+=(f"{header}: Missing\n")
        return result
    def server_info(response):
        return "Server Info: "+ response.headers.get("Server", "Not disclosed")
    def res_header(response):
        result = "\nResponse Headers:\n"
        for key, value in response.headers.items():
            result += f"{key}: {value}\n"
        return result
    def check_redirects(response):
        if response.history:
            result = "\nRedirect Chain:\n"
            for resp in response.history:
                result += f"{resp.status_code} -> {resp.url}\n"
            result += f"Final Destination -> {response.url}\n"
        else:
            result = "\nNo redirects detected.\n"
        return result


    while True: #*!Avoided Program shutdown if link = invalid by using loop!*#
        url = input("Enter the url: ")

        if not url.startswith("http://") and not url.startswith("https://"):
            link = "https://" + url
        else:
            link = url

        try:
            r = requests.get(link, timeout=5)
            break 

        except requests.exceptions.RequestException:#*!Avoided [requests.exceptions.ConnectionError] by checking the link with requests.exceptions.RequestException!*#
            print("Invalid or unreachable link. Please try again.\n")
    if r.status_code >= 500:
        print("Website not available.")
    else:
        print(f"Website reachable. Status Code: {r.status_code}")
 
    while True:
        try:
            print("\n1.Website html code")
            print("2.Website content length")
            print("3.Website status code")
            print("4.Https check")
            print("5.Server Information")
            print("6.Show Response Headers")
            print("7.Security Header Analysis")
            print("8.Check Redirect History")
            print("9.Save Report in a file")
            print("10.EXIT\n")

            choice = int(input("choice: "))

            match choice:
                case 1:
                    print(r.text)
                case 2:
                    print(len(r.content))
                case 3:
                    print(r.status_code)
                case 4:
                    if link.startswith("https://"):
                        print("Secure Connection: Yes")
                    else:
                        print("Secure Connection: No")
                case 5:
                    print(server_info(r))
                case 6:
                    print(res_header(r))
                case 7:
                    print(check_security_headers(r))
                case 8:
                    print(check_redirects(r))
                case 9:
                    while True:
                        try:
                            print("=============================")
                            print("=========FILE SAVING=========")
                            print("=========1.Status============")
                            print("========2.Html Code==========")
                            print("======3.Content-Length=======")
                            print("=4.Security Headers Analysis=")
                            print("=======5.Server Info=========")
                            print("===6.Show Response Headers===")
                            print("====7.Redirection History====")
                            print("===========8.EXIT============")
                            print("=============================")
                            choice2 = int(input("choice: "))
                            match choice2:
                                case 1:
                                    with open("report.txt", "a") as f:
                                        f.write("\nStatus Code: " + str(r.status_code)+"\n")
                                case 2:
                                    with open("report.txt", "a") as f:
                                        f.write("\nHTML Code: " + str(r.text)+"\n")
                                case 3:
                                    with open("report.txt", "a") as f:
                                        f.write("\nCONTENT LENGTH: " + str(len(r.content))+"\n")
                                case 4:
                                    with open("report.txt", "a") as f:
                                        f.write(check_security_headers(r)+"\n")
                                case 5:
                                    with open("report.txt", "a") as f:
                                        f.write(server_info(r) + "\n")
                                case 6:
                                    with open("report.txt", "a") as f:
                                        f.write((res_header(r))+"\n")
                                case 7:
                                    with open("report.txt", "a") as f:
                                        f.write((check_redirects(r))+"\n")
                                case 8:
                                    print("Exiting Report Saving.")
                                    break
                        except ValueError:
                            print("value error")   
                case 10:
                    print("Exiting program...")
                    break
                case _:
                    print("Invalid choice. Try again.")

        except ValueError:#*!Prevented ValueError*!#
            print("Please enter a valid number.")
def subdomain_finder():
    count=0
    domain=input("Enter a domain name(example:google.com): ")
    sub_domains=["www","blog","mail","shop","dev",'api','stage','staging','test','demo','support','help',
                'app','portal','admin','cdn','secure','docs','images','webmail']
    for sub in sub_domains:
        fulldom = sub + "." + domain
        try:
            ip = socket.gethostbyname(fulldom)
            print("the ip of",fulldom,"is",ip)
            count+=1
        except socket.gaierror:
            pass
    print("there are",count,"subdomains of this domain")
while True:
    try:
        print("1.Web-recon-Tool")
        print("2.Subdomain Finder")
        print("3.EXIT")
        choi=int(input("Input the choice: "))
        match choi:
            case 1:
                web_recon()
            case 2:
                subdomain_finder()
            case 3:
                break
            case _:
                print("Invalid Choice")
    except:
        print("Invalid choice")