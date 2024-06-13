"""
Basic list operations
"""
five_number = []
for i in range(1, 6):
    five_number.append(int(input("Number: ")))
print(f"The first number is {five_number[0]}")
print(f"The last number is {five_number[-1]}")
print(f"The smallest number is {min(five_number)}")
print(f"The largest number is {max(five_number)}")
print(f"The average of the numbers is {sum(five_number)/len(five_number)}")

"""
Woefully inadequate security checker
"""
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

if input("Enter the User name: ") in usernames:
    print("Access granted")
else:
    print("Access denied")
