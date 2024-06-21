user_email = input("Email: ")
total_information = {}
while user_email != "":
    name = (" ".join(str(user_email.split("@")[0]).split("."))).title()
    user_input = input(f"Is your name {name}? (Y/n)").lower()
    if user_input == "no" or user_input == "n":
        name = input("Name: ").title()
    total_information[name] = user_email
    user_email = input("Email: ")
print()
for information in total_information:
    print(f"{information} ({total_information[information]})")
