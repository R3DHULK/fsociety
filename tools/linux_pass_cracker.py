import crypt,time
try:
	password = open("password.txt", 'r')
	for passwd in password.readlines():
		passwd = passwd.strip("\n").strip("\r")
		var = crypt.crypt(passwd,"$6$"+"8HOLitkI")
		if var == "$6$8HOLitkI$9HECw2MBzISI1O.RoyJdfugy4VHsTOU4RDTewcFECnZdWLpmtVwNo5a1/hg2kw4Qu74F08eMEwpLdK1eovfEd/":
			print("\033[94m [+] Password Found: ", passwd )
			break
		else:
			print("\033[92m [*] Trying....")
except KeyboardInterrupt:
	print("\n \033[91m[-] KeyBoard Interrupted")
time.sleep(4)
