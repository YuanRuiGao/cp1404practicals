from prac_07.guitar import Guitar


def main():
    """Control program operation"""
    guitars = read_file()
    user_input(guitars)
    display_guitars(guitars)
    save_into_file(guitars)


def read_file():
    """Read file contents and import"""
    guitars = []
    with open("guitars.csv", "r") as guitars_information:
        for line in guitars_information:
            parts = line.strip().split(",")
            guitars.append(Guitar(parts[0], int(parts[1]), float(parts[2])))
    return guitars


def user_input(guitars):
    """User enters new guitar information"""
    guitar_name = input("Name: ")
    while guitar_name != "":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: "))
        guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))
        guitar_name = input("Name: ")


def display_guitars(guitars):
    """Display all sorted guitar data"""
    guitars.sort()
    for i in guitars:
        print(i.name, i.year, i.cost)


def save_into_file(guitars):
    """Save into File"""
    with open("guitars.csv", "w") as guitars_information:
        for line in guitars:
            print(f"{line.name}, {line.year}, {line.cost}", file=guitars_information)


main()
