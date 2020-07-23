import itertools
import os

print("\n")
print(r""" /$$$$$$$$ /$$                 /$$$$$$$                      /$$ /$$      /$$                           /$$ /$$ /$$             /$$    
|__  $$__/| $$                | $$__  $$                    | $$| $$  /$ | $$                          | $$| $$|__/            | $$    
   | $$   | $$$$$$$   /$$$$$$ | $$  \ $$ /$$  /$$  /$$  /$$$$$$$| $$ /$$$| $$  /$$$$$$   /$$$$$$   /$$$$$$$| $$ /$$  /$$$$$$$ /$$$$$$  
   | $$   | $$__  $$ /$$__  $$| $$$$$$$/| $$ | $$ | $$ /$$__  $$| $$/$$ $$ $$ /$$__  $$ /$$__  $$ /$$__  $$| $$| $$ /$$_____/|_  $$_/  
   | $$   | $$  \ $$| $$$$$$$$| $$____/ | $$ | $$ | $$| $$  | $$| $$$$_  $$$$| $$  \ $$| $$  \__/| $$  | $$| $$| $$|  $$$$$$   | $$    
   | $$   | $$  | $$| $$_____/| $$      | $$ | $$ | $$| $$  | $$| $$$/ \  $$$| $$  | $$| $$      | $$  | $$| $$| $$ \____  $$  | $$ /$$
   | $$   | $$  | $$|  $$$$$$$| $$      |  $$$$$/$$$$/|  $$$$$$$| $$/   \  $$|  $$$$$$/| $$      |  $$$$$$$| $$| $$ /$$$$$$$/  |  $$$$/
   |__/   |__/  |__/ \_______/|__/       \_____/\___/  \_______/|__/     \__/ \______/ |__/       \_______/|__/|__/|_______/    \___/  """)
print("\n")

print("Welcome to ThePwdWordlist, this is a tool to create a wordlist based on information you give them!")
print("If you don't know one of the fields below just press ENTER!\n")
print("1) Start wordlist generator\nx) Exit")

option = input("\noption: ")

if option == "1":
    firstname = input("Firstname> ")
    lastname = input("Lastname> ")
    year = input("Year they were born> ")
    mothername = input("Mother's name> ")
    fathername = input("Father's name> ")
    petname = input("Pet's name> ")
    work = input("Where they work> ")
    extra = input("Extra info (Seperate with a comma ',')> ")


    not_formatted_info = [firstname,lastname,year,mothername,fathername,petname] + extra.split(",")
    info = []

    for i in not_formatted_info:
        if not i:
            pass
        else:
            info.append(i)

    wordlist = ""
    for i in range(1,len(info) + 2):
        wordlist_obj = itertools.permutations(info, i)
        for j in wordlist_obj:
            word = "".join(j)
            arrJ = list(j)
            for k in range(len(arrJ)):
                arrJ[k] = list(arrJ[k])
            arrJ[0][0] = arrJ[0][0].upper()
            for k in range(len(arrJ)):
                arrJ[k] = "".join(arrJ[k])
            wordCap = "".join(arrJ)
            lstAllCap = list(j)
            for k in range(len(lstAllCap)):
                lstAllCap[k] = list(lstAllCap[k])
                lstAllCap[k][0] = lstAllCap[k][0].upper()
                lstAllCap[k] = "".join(lstAllCap[k])

            wordlist += "".join(lstAllCap) + "\n"
            wordlist += "_".join(lstAllCap) + "\n"
            wordlist += ".".join(lstAllCap) + "\n"
            wordlist += "_".join(j) + "\n"
            wordlist += ".".join(j) + "\n"
            wordlist += word + "\n"
            wordlist += wordCap + "\n"

    print("\n")

    filename = input("Enter filename> ")

    with open(filename, "w") as file:
        file.write(wordlist)
elif option == "99":
    os.system("clear")
    exit()