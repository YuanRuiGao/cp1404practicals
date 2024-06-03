"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""
MENU = "(H)ello\n(G)oodbye\n(Q)uit\n>>> "

name = input("Enter name: ")
choice = input(MENU).upper()

while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    choice = input(MENU).upper()

print("Finished")
