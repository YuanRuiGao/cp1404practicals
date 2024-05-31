MENU = ("C - Convert Celsius to Fahrenheit\n"
        "F - Convert Fahrenheit to Celsius\n"
        "Q - Quit")


def main():
    """The main function for control flow"""

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = calculate_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = calculate_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def calculate_fahrenheit(celsius):
    """Input Celsius and calculate Fahrenheit and return"""

    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def calculate_celsius(fahrenheit):
    """Input Fahrenheit and calculate Celsius and return"""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()
