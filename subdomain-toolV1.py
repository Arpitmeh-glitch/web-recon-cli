import socket
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
        print(fulldom,"does not exist")
        pass
print(count)
