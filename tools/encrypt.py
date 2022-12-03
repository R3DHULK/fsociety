from crypto import password_encrypt
from getpass import getpass
import sys,time
try:
	def slowprint(s):
		for c in s + '\n' :
			sys.stdout.write(c)
			sys.stdout.flush()
			time.sleep(100 / 1000)
	slowprint("\033[92m [*] Encrypt Your Message :")
	print("=================================")
	def encrypt():
		message = input("\n\033[92m [*] Enter message to encrypt: ")
		password = getpass("\033[92m [*] Enter a password (password will be hidden): ")
		repeated_password = getpass("\033[92m [*]Repeate your password (password will be hidden): ")

		if password != repeated_password:
			print("ERROR: Passwords don't match")
			return
		
		encrypted = password_encrypt(message=message, password=password)
		
		print(encrypted)

	if __name__ == "__main__":
		encrypt()
except KeyboardInterrupt:
	slowprint("\n\033[91m [-] Exiting...")
input(" Enter To Exit")
