from crypto import password_decrypt
from getpass import getpass
import sys,time
try:
	def slowprint(s):
		for c in s + '\n' :
			sys.stdout.write(c)
			sys.stdout.flush()
			time.sleep(100 / 1000)
	slowprint("\033[92m [*] Decrypt Your Message :")
	print("=================================")
	def decrypt():
		message = input("\n\033[92m [*] Enter Encrypted Message: ")
		password = getpass("\033[92m [*] Enter The password (password will be hidden): ")    
		encrypted = password_decrypt(token=message, password=password)
		print(encrypted)

	if __name__ == "__main__":
		decrypt()
except KeyboardInterrupt:
	slowprint("\n\033[91m [-] Exiting...")
input(" Enter To Exit")
