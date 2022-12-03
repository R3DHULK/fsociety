# Python program to test
# internet speed
import os
import speedtest
os.system("clear")
try:
	print('''
  ___                  _   _____       _           
 / __|_ __  ___ ___ __| | |_   _|__ __| |_ ___ _ _ 
 \__ \ '_ \/ -_) -_) _` |   | |/ -_|_-<  _/ -_) '_|
 |___/ .__/\___\___\__,_|   |_|\___/__/\__\___|_|  
     |_|                                           	
	
	''')
	st = speedtest.Speedtest()

	option = int(input(''' [*] What speed do you want to test:

 1) Download Speed

 2) Upload Speed

 3) Ping

 [+] Your Choice: '''))
	print("\n [+] Processing Your Command .... \n\t Please Wait....\n")

	if option == 1:

		print(" [*] Your Download Speed Is" , st.download())

	elif option == 2:

		print(" [*] Your Upload Speed Is" , st.upload())

	elif option == 3:

		servernames =[]

		st.get_servers(servernames)

		print(" [*] Your Ping Result is" , st.results.ping)

	else:

		print(" [+] Please enter the correct choice !")
except KeyboardInterrupt:
	print("\n [-] CTRL + C Detected....Exiting...\n")
input("\n Enter To Exit")
