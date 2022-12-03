import sys,time
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 100)
try:
	running = True 
	print(" Calculator")
	print("================================")
	while running:
		slowprint ("\033[95m 1 = Addition")
		slowprint ("\033[95m 2 = Subtraction")
		slowprint ("\033[95m 3 = Multiplication")
		slowprint ("\033[95m 4 = Division")
		slowprint ("\033[95m 5 = Exit program")
		cmd = int(input("\n\033[92m [*] Choose Option : "))
		if cmd == 1:
			slowprint ("\n Addition")
			print("================================")
			first = int(input(" [+] Enter first number : "))
			second = int(input(" [*] Enter second number : "))
			result = first + second
			slowprint("\n\033[93m OH! It's easy to calculate")
			print (" The Result Is ",first," + ",second," = ",result)
			print (" ")
		elif cmd == 2:
			slowprint ("\n Subtraction")
			print("================================")
			first = int(input(" [*] Enter first number : "))
			second = int(input(" [*] Enter second number : "))
			result = first - second
			slowprint("\n\033[93m OH! It's easy to calculate")
			print (" The Result Is ",first," - ",second," = ",result)
			print (" ")
		elif cmd == 3:
			slowprint ("\n Multiplication")
			print("================================")
			first = int(input(" [*] Enter first number : "))
			second = int(input(" [*] Enter second number : "))
			result = first * second
			slowprint("\n\033[93m OH! It's easy to calculate")
			print (" The Result Is ",first," x ",second," = ",result)
			print (" ")
		elif cmd == 4:
			slowprint ("\n Division")
			print("================================")
			first = int(input(" [*] Enter first number : "))
			second = int(input(" [*] Enter second number : "))
			slowprint("\n\033[93m OH! It's easy to calculate")
			result = first / second
			print (" The Result Is ",first," : ",second," = ",result)
			print (" ")
		elif cmd == 5:
			slowprint( "\n ***HULK offers you a good bye :D ***")
			running = False
		else:
			slowprint(' Are YOU OUT OF YOUR MIND? Huh!')
except ZeroDivisionError:
	print(" 0 devided by 0 is infinite")
except KeyboardInterrupt:
	slowprint("\n [-] Exiting")
time.sleep(0.4)
