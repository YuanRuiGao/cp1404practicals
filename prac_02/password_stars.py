password = input("please enter your password\n")
while password == "":
    print("error, please enter the right password")
    password = input("please enter your password\n")
print(len(password) * "*")
