import requests
import urllib.parse
from bs4 import BeautifulSoup

print(r'''
   ___                _       ___          _   
  / __|___  ___  __ _| |___  |   \ ___ _ _| |__
 | (_ / _ \/ _ \/ _` | / -_) | |) / _ \ '_| / /
  \___\___/\___/\__, |_\___| |___/\___/_| |_\_\
                |___/https://github.com/R3DHULK                                                   
														
	''')	
try:
	blacklist = ['support.google.com', 'accounts.google.com']

	dorks = input("\033[92m [*] Enter Your dork: ")
	page_num = input("\033[92m [*] Enter Page Number: ")
	int_page_num = int(page_num)
	mainurl = f"https://www.google.com/search?q={dorks}&start="


	proxie = {
		'http': "88.198.50.103:3128",
		'http': "88.198.24.108:8080",
		'http': "176.9.75.42:3128",
	}

	def single_scrap(url, page, proxie):
		try:

			request = requests.get(url+str(page), proxies=proxie).text

			soup = BeautifulSoup(request, 'html.parser')

			links = soup.findAll('a')

			idnt = "&sa"
			for x in links:
				y = x['href']
				if y.startswith("/url?q="):
					gg = y.replace("/url?q=", "")
					hr = gg.split("&sa=")
					hk = hr[0]
					gf = hk.split("//")[1]
					k = gf.split("/")[0]
					if k in blacklist:
						pass
					else:
						enc = urllib.parse.unquote(hk)
						print(enc)
						out = open("output.txt", "a")
						out.write(enc+"\n")
						out.close()
		except Exception:
			pass
			
			
	page = 0

	for x in range(int_page_num):
		single_scrap(mainurl, page, proxie)
		page += 10
except KeyboardInterrupt:
	print("\n\033[91m [-] Exiting")
except ValueError:
	print("\n\033[91m [-] Please Give Value")
input("\033[93m [-] Enter To Exit")
