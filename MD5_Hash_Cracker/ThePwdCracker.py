import os
import hashlib
import itertools
import string
import win32com.client as wincl

speak = wincl.Dispatch("SAPI.SpVoice")

print("\n")
print(r"""/$$$$$$$$ /$$                 /$$$$$$$                      /$$  /$$$$$$                               /$$                                
|__  $$__/| $$                | $$__  $$                    | $$ /$$__  $$                             | $$                                
   | $$   | $$$$$$$   /$$$$$$ | $$  \ $$ /$$  /$$  /$$  /$$$$$$$| $$  \__/  /$$$$$$  /$$$$$$   /$$$$$$$| $$   /$$  /$$$$$$   /$$$$$$       
   | $$   | $$__  $$ /$$__  $$| $$$$$$$/| $$ | $$ | $$ /$$__  $$| $$       /$$__  $$|____  $$ /$$_____/| $$  /$$/ /$$__  $$ /$$__  $$      
   | $$   | $$  \ $$| $$$$$$$$| $$____/ | $$ | $$ | $$| $$  | $$| $$      | $$  \__/ /$$$$$$$| $$      | $$$$$$/ | $$$$$$$$| $$  \__/      
   | $$   | $$  | $$| $$_____/| $$      | $$ | $$ | $$| $$  | $$| $$    $$| $$      /$$__  $$| $$      | $$_  $$ | $$_____/| $$            
   | $$   | $$  | $$|  $$$$$$$| $$      |  $$$$$/$$$$/|  $$$$$$$|  $$$$$$/| $$     |  $$$$$$$|  $$$$$$$| $$ \  $$|  $$$$$$$| $$            
   |__/   |__/  |__/ \_______/|__/       \_____/\___/  \_______/ \______/ |__/      \_______/ \_______/|__/  \__/ \_______/|__/           """)
print("\n")

print("1) Custom Wordlist\n2) 100 most common passwords\n3) 10000 most common passwords\n4) Every possible combination\n5) Every possible combination (only numbers)\nx) Exit")

option = input("option: ")
if option == "1":
	wordlist = input("Enter the path to the wordlist: ")
	with open(wordlist, "r") as file:
		content = file.read().split("\n")
		passhash = input("Enter the password hash: ")
		passw = False
		for i in content:
			encrypted_pass = hashlib.md5(i.encode()).hexdigest()
			if encrypted_pass == passhash:
				print(f"Password: {i}")
				passw = True

		if passw == True:
			print("Password is cracked!")
			input("Press ENTER to continue!")
			os.system("cls")
		else:
			print("Password not cracked!")
			input("Press ENTER to continue!")
			os.system("cls")
		file.close()
elif option == "2":
	with open("MD5_Hash_Cracker/prewordlists/100_passwords.txt", "r") as file:
		content = file.read().split("\n")
		passhash = input("Enter the password hash: ")
		passw = False
		for i in content:
			cipher_pass = hashlib.md5(i.encode()).hexdigest()
			if cipher_pass == passhash:
				print(f"Password: {i}")
				passw = True

		if passw == True:
			print("Password is cracked!")
			input("Press ENTER to continue!")
			os.system("cls")
		else:
			print("Password not cracked!")
			input("Press ENTER to continue!")
			os.system("cls")
		file.close()
elif option == "3":
	with open("MD5_Hash_Cracker/prewordlists/10000_passwords.txt", "r") as file:
		content = file.read().split("\n")
		passhash = input("Enter the password hash: ")
		passw = False
		for i in content:
			encrypted_pass = hashlib.md5(i.encode()).hexdigest()
			if passhash == encrypted_pass:
				print(f"Password: {i}")
				passw = True
		if passw == True:
			print("Password is cracked!")
			input("Press ENTER to continue!")
			os.system("cls")
		else:
			print("Password not cracked!")
			input("Press ENTER to continue!")
			os.system("cls")
		file.close()
elif option == "4":
	length = input("Enter the range (x-y): ").split("-")
	passhash = input("Enter the password hash: ")
	alpha = list(string.ascii_lowercase) + list(string.ascii_uppercase) + list("0123456789") + list("~`!@#$%^&*()-_+=,.<>?/:;{}[]|")
	for i in range(int(length[0]), int(length[1])):
		combinations_obj = itertools.product(alpha, repeat=i)
		for j in combinations_obj:
			encrypted_pass = hashlib.md5("".join(j).encode()).hexdigest()
			if encrypted_pass == passhash:
				print(f"Password: {''.join(j)}")
				print("Password is cracked!")
				speak.speak("Password is cracked!")
				input("Press ENTER to continue!")
				os.system("cls")
				exit()
	print("Password is not cracked!")
	speak.speak("Password is not cracked!")
	input("Press ENTER to continue!")
	os.system("cls")
	exit()
elif option == "5":
	length = input("Enter the range (x-y): ").split("-")
	passhash = input("Enter the password hash: ")
	alpha = list("0123456789")
	for i in range(int(length[0]), int(length[1])):
		combinations_obj = itertools.product(alpha, repeat=i)
		for j in combinations_obj:
			encrypted_pass = hashlib.md5("".join(j).encode()).hexdigest()
			if encrypted_pass == passhash:
				print(f"Password: {''.join(j)}")
				print("Password is cracked!")
				speak.speak("Password is cracked!")
				input("Press ENTER to continue!")
				os.system("cls")
				exit()
	print("Password is not cracked!")
	speak.speak("Password is not cracked!")
	input("Press ENTER to continue!")
	os.system("cls")
	exit()
elif option == "x":
	os.system("cls")
	exit()