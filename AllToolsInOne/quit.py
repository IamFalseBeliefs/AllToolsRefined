def quitit():
	import os
	from termcolor import colored
	import start
	c = colored
	print(c("[----] Are you sure you want to leave?", "red"))
	print(c("[----] 1", "red"))
	print(c("[----] 2", "green"))
	gatto = int(input(c("[----] Type 1 to exit; 2 to continue: ")))
	if gatto == 1:
		os.system("clear")
		exit(0)
	elif gatto == 2:
		os.system("clear")
		startbegin()