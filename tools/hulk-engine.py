try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
 
print('''\033[92m
  _  _ _   _ _    _  __  ___           _          
 | || | | | | |  | |/ / | __|_ _  __ _(_)_ _  ___ 
 | __ | |_| | |__| ' <  | _|| ' \/ _` | | ' \/ -_)
 |_||_|\___/|____|_|\_\ |___|_||_\__, |_|_||_\___|
    © Sumalya Chatterjee         |___/              
  \033[92m ''')
try:
	# to search
	query = input("\033[92m [*] Search Here : ")
	for j in search(query, tld="co.in", num=10, stop=10, pause=2):
		print("")
		print(j)
except KeyboardInterrupt:
	print("\033[91m\n [-] Ctrl+C Detected")
input("\n[-] Enter To Exit")
