import os
import sys
import socket
import datetime
import time
import psutil

FILE = os.path.join(os.getcwd(), "networkinfo.log")

# creating log file in the currenty directory
# ??getcwd?? get current working directory,
# os function, ??path?? to specify path

try:
	def ping():
		# to ping a particular IP
		try:
			socket.setdefaulttimeout(3)
		
			# if data interruption occurs for 3
			# seconds, <except> part will be executed

			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			# AF_INET: address family
			# SOCK_STREAM: type for TCP

			host = "8.8.8.8"
			port = 53

			server_address = (host, port)
			s.connect(server_address)

		except OSError as error:
			return False
			# function returns false value
			# after data interruption

		else:
			s.close()
			# closing the connection after the
			# communication with the server is completed
			return True


	def calculate_time(start, stop):

		# calculating unavailability
		# time and converting it in seconds
		difference = stop - start
		seconds = float(str(difference.total_seconds()))
		return str(datetime.timedelta(seconds=seconds)).split(".")[0]

	def first_check():
		# to check if the system was already
		# connected to an internet connection

		if ping():
			# if ping returns true
			live = "\n \033[92m✔️✔️✔️ CONNECTION ACQUIRED\n"
			print(live)
			connection_acquired_time = datetime.datetime.now()
			acquiring_message = " \033[92m✔️✔️✔️ Connection Acquired At: " + \
				str(connection_acquired_time).split(".")[0]
			print(acquiring_message)

			with open(FILE, "a") as file:
		
				# writes into the log file
				file.write(live)
				file.write(acquiring_message)

			return True

		else:
			# if ping returns false
			not_live = "\n\033[91m ❌❌❌ CONNECTION NOT ACQUIRED\n"
			print(not_live)

			with open(FILE, "a") as file:
		
				# writes into the log file
				file.write(not_live)
			return False


	def main():

		# main function to call functions
		monitor_start_time = datetime.datetime.now()
		monitoring_date_time = "\033[92m [+] Monitoring Started At: " + \
			str(monitor_start_time).split(".")[0]
		if first_check():
			# if true
			print(monitoring_date_time)
			# monitoring will only start when
			# the connection will be acquired

		else:
			# if false
			while True:
		
				# infinite loop to see if the connection is acquired
				if not ping():
				
					# if connection not acquired
					time.sleep(1)
				else:
				
					# if connection is acquired
					first_check()
					print(monitoring_date_time)
					break

		with open(FILE, "a") as file:
	
			# write into the file as a into networkinfo.log,
			# "a" - append: opens file for appending,
			# creates the file if it does not exist???
			file.write("\n")
			file.write(monitoring_date_time + "\n")

		while True:
	
			# infinite loop, as we are monitoring
			# the network connection till the machine runs
			if ping():
			
				# if true: the loop will execute after every 5 seconds
				time.sleep(5)

			else:
				# if false: fail message will be displayed
				down_time = datetime.datetime.now()
				fail_msg = "\033[91m ❌❌❌ Disconnected At: " + str(down_time).split(".")[0]
				print(fail_msg)

				with open(FILE, "a") as file:
					# writes into the log file
					file.write(fail_msg + "\n")

				while not ping():
			
					# infinite loop, will run till ping() return true
					time.sleep(1)

				up_time = datetime.datetime.now()
			
				# after loop breaks, connection restored
				uptime_message = "\033[92m connected again: " + str(up_time).split(".")[0]

				down_time = calculate_time(down_time, up_time)
				unavailablity_time = " \033[92mconnection was unavailable for: " + down_time

				print(uptime_message)
				print(unavailablity_time)

				with open(FILE, "a") as file:
				
					# log entry for connection restoration time,
					# and unavailability time
					file.write(uptime_message + "\n")
					file.write(unavailablity_time + "\n")
	def slowprint(s):
		for c in s + '\n' :
			sys.stdout.write(c)
			sys.stdout.flush()
			time.sleep(10. / 100)
	slowprint(" \n\033[93m Press Ctrl+C To Do Network Monitoring")
	slowprint(" \n\033[91m Double Press Ctrl+C To Exit Tool")
	main()
	
except KeyboardInterrupt:
	slowprint("\n\033[90m [*] You Have Entered Ctrl+C....Entering Into Network Monitor Mode.... ")

UPDATE_DELAY = 1 # in seconds
try:
	def get_size(bytes):
		"""
		Returns size of bytes in a nice format
		"""
		for unit in ['', 'K', 'M', 'G', 'T', 'P']:
			if bytes < 1024:
				return f"{bytes:.2f}{unit}B"
			bytes /= 1024

	# get the network I/O stats from psutil
	io = psutil.net_io_counters()
	# extract the total bytes sent and received
	bytes_sent, bytes_recv = io.bytes_sent, io.bytes_recv
	def slowprint(s):
		for c in s + '\n' :
			sys.stdout.write(c)
			sys.stdout.flush()
			time.sleep(10. / 100)
	slowprint("\n \033[92m      [+] Network Monitoring Is On Progress : ")
	time.sleep(2)
	while True:
		# sleep for `UPDATE_DELAY` seconds
		time.sleep(UPDATE_DELAY)
		# get the stats again
		io_2 = psutil.net_io_counters()
		# new - old stats gets us the speed
		us, ds = io_2.bytes_sent - bytes_sent, io_2.bytes_recv - bytes_recv
		# print the total download/upload along with current speeds
		print(f"Upload: {get_size(io_2.bytes_sent)}   "
			f", Download: {get_size(io_2.bytes_recv)}   "
			f", Upload Speed: {get_size(us / UPDATE_DELAY)}/s   "
			f", Download Speed: {get_size(ds / UPDATE_DELAY)}/s      ", end="\r")
		# update the bytes_sent and bytes_recv for next iteration
		bytes_sent, bytes_recv = io_2.bytes_sent, io_2.bytes_recv
except KeyboardInterrupt:
	slowprint("\n\n\033[91m [-] Ctrl+C Detected.....Exiting.....")    
time.sleep(2)
