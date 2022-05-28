import os
from termcolor import colored
import start
c = colored
def vulnb():
	print("\n")
	print(c("[----] Continue using Vuln-Ture [1]", "green"))
	print(c("[----] Go back to main screen [2]", "red"))
	option1 = int(input(c("[----] Chose an option: ")))
	if option1 == 2:
		os.system("clear")
		start.begin()
	elif option1 == 1:
		import portscan2
		print(c("   __      __    _                  _                   ", "red"))
		print(c("   \ \    / /   | |                | |                  ", "green"))
		print(c("    \ \  / /   _| |_ __    ______  | |_ _   _ _ __ ___  ", "magenta"))
		print(c("     \ \/ / | | | | '_ \  |______| | __| | | | '__/ _ \ ", "red"))
		print(c("      \  /| |_| | | | | |          | |_| |_| | | |  __/ ", "green"))
		print(c("       \/  \__,_|_|_| |_|           \__|\__,_|_|  \___| ", "red"))
		print("<<<<<----->= Vulnerablity Scanner By: IAmFalseBeliefs <=----->>>>>")
		print("    <<<<<----->=          Ports Made Easy         <=----->>>>>")
		print("\n")         

		targets_ip = input("[----] Enter target to scan for vulnerable ports: ")
		port_number = int(input("[----] Enter port number to scan to (500 is from port 1 to 500): "))
		vulnfile = input("[----] Enter path to file with vulnerable softwares: ")
		print("\n")

		target = portscan2.PortScan(targets_ip, port_number)
		target.scan()

		with open(vulnfile, "r") as file:
			count = 0
			for banner in target.banners:
				file.seek(0)
				for line in file.readlines():
					if line.strip() in banner:
						print(c("[----] Vulnerable Banner: " + banner + "On Port: " + str(target.open_ports[count]), "green"))
				count += 1