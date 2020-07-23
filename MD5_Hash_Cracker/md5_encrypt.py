import hashlib

password = input("Enter the password: ")

print(hashlib.md5(password.encode()).hexdigest())
