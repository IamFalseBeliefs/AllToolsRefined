import os
from termcolor import colored
import start
c = colored
def pscanner123():
	print("\n")
	print(c("[----] Continue using PortScanner [1]", "green"))
	print(c("[----] Go back to main screen [2]", "red"))
	option1 = int(input(c("[----] Chose an option: ")))
	if option1 == 2:
		os.system("clear")
		start.begin()
	elif option1 == 1:
		import socket
		from IPy import IP

		print(c("     _____           __     _____                                  ", "green"))
		print(c("    |  __ \         | |    / ____|                                 ", "white"))
		print(c("    | |__) |__  _ __| |_  | (___   ___ __ _ _ __  _ __   ___ _ __  ", "blue"))
		print(c("    |  ___/ _ \| '__| __|  \___ \ / __/ _` | '_ \| '_ \ / _ \ '__| ", "red"))
		print(c("    | |  | (_) | |  | |_   ____) | (_| (_| | | | | | | |  __/ |    ", "yellow"))
		print(c("    |_|   \___/|_|   \__| |_____/ \___\__,_|_| |_|_| |_|\___|_|    ", "white"))  
		print("\n")
		print("     <<<<<----->= Port Scanner By: IAmFalseBeliefs <=----->>>>>")
		print("     <<<<<----->=          Ports Made Easy         <=----->>>>>")
		print("<<<<<----->= Use NMAP to find version of service running <=----->>>>>")
		print("\n")

		def check_ip(ip):
			try:
				IP(ip)
				return(ip)
			except ValueError:
				return socket.gethostbyname(ip)

		def get_banner(s):
			return s.recv(1024)

		def scan_port(ipaddress, port):
			try:
				sock = socket.socket()
				sock.settimeout(float(speed))
				sock.connect((ipaddress, port))
				try:
					banner = get_banner(sock)
					print(c("[----] Port " + str(port) + " is open <-----> running " + str(banner.decode().strip("\n")), "green"))
				except:
					print(c("[----] Port " + str(port) + " is open <-----> No Banner Avaliable", "cyan"))
			except:
				pass

		targets = input("[----] Enter URL or IP address to scan (Split multiple targets by coma): ")
		speed = input("[----] Enter speed (suggested 0.5 for most acuracy): ")
		range1 = input("[----] Please put number of begining port (ie. 80): ")
		range2 = int(input("[----] Please put number of ending port (ie. 100): "))
		range2 += 1

		def scant(target):
			converted_ip = check_ip(target)
			print("\n " + "     <<<<<----->= Scanning " + str(target) + " <=----->>>>>")
			for port in range(int(range1), int(range2)):
				scan_port(converted_ip, port)

		if "," in targets:
			for ip_add in targets.split(","):
				scant(ip_add.strip(" "))
		else:
			scant(targets)
