import random
import pyautogui
import os
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLOPMNQRSTUVWXYZ@#$*!-_=+&%0123456789"

allchar=list(chars)

pwd = pyautogui.password(" Enter A Password : ")
sample_pwd = " "
try:
	while(sample_pwd != pwd):
		sample_pwd = random.choices(allchar, k=len(pwd))
	
		print("<==========================="+ str(sample_pwd)+ "==================================>")
	
		if (sample_pwd == list(pwd)):
			print(" [+] Your Password IS : "+ "".join(sample_pwd))
			break
except KeyboardInterrupt:
	print("\n [-] Ctrl+C Detected.....Exiting")
input(" [+] Enter To Exit")
