import pyperclip
import requests
import random
import string
import time
import sys
import re
import os

API = 'https://www.1secmail.com/api/v1/'
domainList = ['1secmail.com', '1secmail.net', '1secmail.org']
domain = random.choice(domainList)

def slowprint(s):
		for c in s + '\n' :
			sys.stdout.write(c)
			sys.stdout.flush()
			time.sleep(10 / 100)
try:			
	def banner():
		print(r'''                                                                               
			▄████  ██   █  █▀ ▄███▄   █▀▄▀█ ██   ▄█ █     
			█▀   ▀ █ █  █▄█   █▀   ▀  █ █ █ █ █  ██ █     
			█▀▀    █▄▄█ █▀▄   ██▄▄    █ ▄ █ █▄▄█ ██ █     
			█      █  █ █  █  █▄   ▄▀ █   █ █  █ ▐█ ███▄  
			 █        █   █   ▀███▀      █     █  ▐     ▀ 
			  ▀      █   ▀              ▀     █           
					▀                        ▀                   
			  domainList = ['1secmail.com','1secmail.net','1secmail.org']
		''')

	def generateUserName():
		name = string.ascii_lowercase + string.digits
		username = ''.join(random.choice(name) for i in range(10))
		return username

	def extract():
		getUserName = re.search(r'login=(.*)&',newMail).group(1)
		getDomain = re.search(r'domain=(.*)', newMail).group(1)
		return [getUserName, getDomain]

	# Got this from https://stackoverflow.com/a/43952192/13276219
	def print_statusline(msg: str):
		last_msg_length = len(print_statusline.last_msg) if hasattr(print_statusline, 'last_msg') else 0
		print(' ' * last_msg_length, end='\r')
		print(msg, end='\r')
		sys.stdout.flush()
		print_statusline.last_msg = msg

	def deleteMail():
		url = 'https://www.1secmail.com/mailbox'
		data = {
			'action': 'deleteMailbox',
			'login': f'{extract()[0]}',
			'domain': f'{extract()[1]}'
		}

		print_statusline("Disposing your email address - " + mail + '\n')
		req = requests.post(url, data=data)

	def checkMails():
		reqLink = f'{API}?action=getMessages&login={extract()[0]}&domain={extract()[1]}'
		req = requests.get(reqLink).json()
		length = len(req)
		if length == 0:
			print_statusline("\033[91m Your mailbox is empty. Hold tight. Mailbox is refreshed automatically every 5 seconds.")
		else:
			idList = []
			for i in req:
				for k,v in i.items():
					if k == 'id':
						mailId = v
						idList.append(mailId)

			x = 'mails' if length > 1 else 'mail'
			print_statusline(f"\033[92m You received {length} {x}. (Mailbox is refreshed automatically every 5 seconds.)")

			current_directory = os.getcwd()
			final_directory = os.path.join(current_directory, r'All Mails')
			if not os.path.exists(final_directory):
				os.makedirs(final_directory)

			for i in idList:
				msgRead = f'{API}?action=readMessage&login={extract()[0]}&domain={extract()[1]}&id={i}'
				req = requests.get(msgRead).json()
				for k,v in req.items():
					if k == 'from':
						sender = v
					if k == 'subject':
						subject = v
					if k == 'date':
						date = v
					if k == 'textBody':
						content = v

				mail_file_path = os.path.join(final_directory, f'{i}.txt')

				with open(mail_file_path,'w') as file:
					file.write("Sender: " + sender + '\n' + "To: " + mail + '\n' + "Subject: " + subject + '\n' + "Date: " + date + '\n' + "Content: " + content + '\n')

	banner()
	userInput1 = input("\n \033[94m[+] Do you wish to use to a custom domain name (Y/N): ").capitalize()

	try:

		if userInput1 == 'Y' or userInput1 == 'y' :
			userInput2 = input("\n \033[90m[+] Enter the name that you wish to use as your domain name: ")
			newMail = f"{API}?login={userInput2}&domain={domain}"
			reqMail = requests.get(newMail)
			mail = f"{extract()[0]}@{extract()[1]}"
			pyperclip.copy(mail)
			slowprint("\n \033[93m Your temporary email is " + mail + " (Email address copied to clipboard.)" +"\n")
			slowprint(f"\033[95m ---------------------------- | Inbox of {mail}| ----------------------------\n")
			while True:
				checkMails()
				time.sleep(5)

		if userInput1 == 'N' or userInput1 == 'n':
			newMail = f"{API}?login={generateUserName()}&domain={domain}"
			reqMail = requests.get(newMail)
			mail = f"{extract()[0]}@{extract()[1]}"
			pyperclip.copy(mail)
			print("\n \033[92mYour temporary email is " + mail + " (Email address copied to clipboard.)" + "\n")
			print(f"\033[91m ---------------------------- | Inbox of {mail} | ----------------------------\n")
			while True:
				checkMails()
				time.sleep(5)

	except(KeyboardInterrupt):
		deleteMail()
		print("\n\033[98m Programme Interrupted")
		os.system('cls' if os.name == 'nt' else 'clear')
except KeyboardInterrupt:
	slowprint("\n\033[91m [-] Exiting....")
time.sleep(2)
