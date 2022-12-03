#!/usr/bin/env python

import subprocess


print(r'''   
  __  __   _   ___     ___ _  _   _   _  _  ___ ___ ___ 
 |  \/  | /_\ / __|__ / __| || | /_\ | \| |/ __| __| _ \
 | |\/| |/ _ \ (_|___| (__| __ |/ _ \| .` | (_ | _||   /
 |_|  |_/_/ \_\___|   \___|_||_/_/ \_\_|\_|\___|___|_|_\
                                                         ''' )
try:
	interface = input("\033[92m [*] Please sepcify the interface: ")
	new_mac = input("\033[92m [*] Please specify new mac: ")

	print(" [!] Changing MAC ADDRESS for " + interface + " to " + new_mac )
	subprocess.call("ifconfig " + interface + " down", shell=True)
	subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
	subprocess.call("ifconfig " + interface + " up", shell=True)
except KeyboardInterrupt:
	print("\n\033[91m [-] Exiting....")
input("\n [+] Press Enter To Exit")
