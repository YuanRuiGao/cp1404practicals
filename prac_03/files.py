"""1"""
NAME = "name.txt"
open_file = open(NAME, "w")
print(input("Enter your name: "), file=open_file)
open_file.close()

"""2"""
open_file = open(NAME, "r")
print(f"Hi {open_file.read()}")
open_file.close()

"""3"""
with open("numbers.txt", "r") as open_file:
    number_one = int(open_file.readline())
    number_two = int(open_file.readline())
result = number_one + number_two
print(result)

"""4"""
result = 0
with open("numbers.txt", "r") as open_file:
    for line in open_file:
        result += int(line)
print(result)
