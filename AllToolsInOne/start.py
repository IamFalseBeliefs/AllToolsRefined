def begin():
	print(c("               _ _   _______          _      ", "green"))
	print(c("         /\   | | | |__   __|        | |     ", "green"))
	print(c("        /  \  | | |    | | ___   ___ | |___  ", "green"))
	print(c("       / /\ \ | | |    | |/ _ \ / _ \| / __| ", "green"))
	print(c("      / ____ \| | |    | | (_) | (_) | \__ \ ", "green"))
	print(c("     /_/    \_\_|_|    |_|\___/ \___/|_|___/ ", "green"))
	print(" <<<<<----->= All Tools By: IAmFalseBeliefs <=----->>>>>")
	print("<<<<<----->=          Ports Made Easy         <=----->>>>>")
	print("\n")
	print(c("[----] Port scanner [1]", "blue"))
	print(c("[----] SSH Brute force [2]", "green"))
	print(c("[----] Vulnerablility Scanner [3]", "cyan"))
	print(c("[----] ARP Spoofer [4]", "yellow"))
	print(c("[----] Password Sniffer [5]", "magenta"))
	print(c("[----] Clear your screen [6]", "white"))
	print(c("[----] Exit [7]", "red"))
	choice = int(input(c("Chose an option: ", "white")))
	print("\n")
	if choice == 1:
		os.system("clear")
		portscanner.pscanner123()
	elif choice == 2:
		os.system("clear")
		sshbrute.sbrute()
	elif choice == 3:
		os.system("clear")
		vulnture.vulnb()
	elif choice == 4:
		os.system("clear")
		arpoof.asp()
	elif choice == 5:
		os.system("clear")
		passniff.passniff()
	elif choice == 6:
		os.system("clear")
		begin()
	elif choice == 7:
		os.system("clear")
		quit.quitit()