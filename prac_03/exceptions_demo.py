"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    When the input value does not meet the storage requirements

2. When will a ZeroDivisionError occur?
    When 0 is divided by any number

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Yes, I added a while outside the whole program. If the program does not meet the requirements,
     it will loop infinitely until the value is available.

"""
not_finish = True
while not_finish:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        print(fraction)
        not_finish = False
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")

print("Finished.")

