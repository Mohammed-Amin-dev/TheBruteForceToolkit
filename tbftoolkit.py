import os
from colorama import Fore
from colorama import Style

os.system("clear")
os.system("title TheBruteForceToolkit")

def main():
	print(Fore.GREEN + Style.BRIGHT + f"""  _____ _          ____             _       _____                 _____           _ _  ___ _   
 |_   _| |__   ___| __ ) _ __ _   _| |_ ___|  ___|__  _ __ ___ __|_   _|__   ___ | | |/ (_) |_ 
   | | | '_ \ / _ \  _ \| '__| | | | __/ _ \ |_ / _ \| '__/ __/ _ \| |/ _ \ / _ \| | ' /| | __|
   | | | | | |  __/ |_) | |  | |_| | ||  __/  _| (_) | | | (_|  __/| | (_) | (_) | | . \| | |_ 
   |_| |_| |_|\___|____/|_|   \__,_|\__\___|_|  \___/|_|  \___\___||_|\___/ \___/|_|_|\_\_|\__|
                                                                                               """ + Style.RESET_ALL)
	print("\n", end="")

	print(f"{Fore.BLUE}{Style.BRIGHT}[---] TheBruteForceToolKit {Fore.WHITE}({Fore.YELLOW}TBFTK{Fore.WHITE}) {Fore.BLUE}[---]{Style.RESET_ALL}")
	print(f"{Fore.BLUE}{Style.BRIGHT}[---] Created by{Fore.RED} Mohammed Amin {Fore.BLUE}    [---]{Style.RESET_ALL}")
	print(f"{Fore.BLUE}{Style.BRIGHT}[---] Version: {Fore.RED}1.0.0{Fore.BLUE}               [---]{Style.RESET_ALL}\n")
	print(f"{Fore.CYAN}{Style.BRIGHT}TheBruteForceToolKit is a collection of tools for password attacks.\nUse this tool responsibly, we are not responsible for what YOU do!{Style.RESET_ALL}\n")

	print(f"{Fore.YELLOW}Select from the menu:{Style.RESET_ALL}")
	print("\n", end="")
	print(f"""{Fore.YELLOW}1) MD5 Hash Cracker
2) Wordlist Generator
3) Auto Password Typing
x) Exit{Style.RESET_ALL}""")
	print("\n", end="")

	while True:
		try:
			option = input(f"{Fore.CYAN}TBFTK{Style.BRIGHT}>{Style.RESET_ALL}")
		except:
			print("\nQUITING!")
			exit()

		if option == "1":
			os.system("cls")
			os.system("python MD5_Hash_Cracker/ThePwdCracker.py")
			main()
		elif option == "2":
			os.system("cls")
			os.system("python Wordlist_generator/ThePwdWordlist.py")
			os.system("cls")
			main()
		elif option == "3":
			os.system("cls")
			os.system("python AutoTypingBruteForce/ThePwdAttacker.py")
			os.system("cls")
			main()
		elif option == "x":
			print("QUITING!")
			exit()
		else:
			print("Enter a correct option!")
			input("Press ENTER to continue!")
			os.system("cls")
			main()

main()
