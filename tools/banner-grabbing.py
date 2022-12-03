import socket,sys,time

logo = '''\033[92m
	  ___                            ___          _    _             
	 | _ ) __ _ _ _  _ _  ___ _ _   / __|_ _ __ _| |__| |__  ___ _ _ 
	 | _ \/ _` | ' \| ' \/ -_) '_| | (_ | '_/ _` | '_ \ '_ \/ -_) '_|
	 |___/\__,_|_||_|_||_\___|_|    \___|_| \__,_|_.__/_.__/\___|_|  
																	
                    coded by Sumalya Chatterjee
'''
print(logo)
try:
	def slowprint(s):
		for c in s + '\n' :
			sys.stdout.write(c)
			sys.stdout.flush()
			time.sleep(10. / 100)
	def ban_grab(host, port, delay) :
		'''
		This function takes three parameters from main() to process and get the banner of the requested port
		It has a specific condition for HTTP port which make this program more flexible than other simple
		banner grabbers

		:param host:        Ask HULK a IP ADDRESS or URL
		:param port:         HULK REQUESTED PORT
		:param delay:      TIME DELAY for SEARCH
		:return:                 None
		'''
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)           # Making a TCP socket
		try :
			s.settimeout(delay)
			if port == 80 :                                             # If user requested port is 80
				s.connect((str(host), port))
				GET = 'GET / HTTP/1.1\nHost: '+ str(host) +'\n\n'       # Request more than ordinary three way handshake
				s.sendall(str.encode(GET))
				banner = s.recvfrom(512)                                # Important part of the banner received

			else :
				s.connect((str(host), port))                            # Trying normal TCP handshake and getting banner
				banner = s.recvfrom(512)

			banner = banner[0]
			banner = banner.splitlines()                                # Processing received banner
			for line in banner:
				line = str(line)
				line = line.replace('\'','')                            # Removing unnecessary part of the line
				print(line[1::])

		except Exception as er :
			slowprint('\033[91m Error : ' + str(er))                                 # Exception handling

		finally :
			s.close()                                                   # Closing socket

	def user_input(msg) :                                               # Checking for keyboard interrupt
		while True :
			try :
				return input(msg)
			except KeyboardInterrupt :
				slowprint('\033[91m [-] HULK does not allowed you to quit right now !')

	def main() :
		host = user_input('\033[92m [+] Ask HULK a IP or URL : ')                         # Taking and validating user inputs
		port = int(user_input('\033[92m [+] Ask HULK a port : '))
		if port < 1 or port > 65535 :
			slowprint('\033[91m [+] Invalid input for port\nDefault set 80')
			port = 80
		delay = int(user_input('\033[92m [+] Enter delay : '))
		if delay < 0 or delay > 100 :
			slowprint('\033[91m [-] Invalid input for delay\nDefault set 5')
			delay = 5
		print('='*30 + 'Banner' +'='*30)
		ban_grab(host, port, delay)                                     # Calling function ban_grab()

	if __name__ == '__main__' :
		main()
except KeyboardInterrupt:
	slowprint(' [-] Exiting....')
