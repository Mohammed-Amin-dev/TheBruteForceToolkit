import re

wordlist = ""

with open("1000_passwords.txt", "r") as file:
    content = file.read().split("\n")
    for i in content:
        wordlist += re.sub("<.*?>", "", i) + "\n"
    file.close()

with open("1000_passwords.txt", "w") as file:
    file.write(wordlist)
    file.close()
