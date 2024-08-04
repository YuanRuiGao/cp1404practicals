from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive\n>>> "
TAXIS = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
         SilverServiceTaxi("Hummer", 200, 4)]


def main():
    """Control program execution"""
    total_cost = 0.0
    current_taxi = None
    print("Let's drive!")

    choice = input(MENU).upper()
    while choice != "Q":
        if choice == "C":
            current_taxi = choice_taxi()
        elif choice == "D":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                current_cost = drive_taxi(current_taxi)
                total_cost += current_cost
                print(f"Your {current_taxi.name} cost you ${current_cost:.2f}")
        else:
            print("Invalid choice!")
        print(f"Bill to date:{total_cost:.2f}")
        choice = input(MENU).upper()
    print(f"Total trip cost: ${total_cost}")
    print("Taxis are now:")
    display_all_taxi()


def choice_taxi():
    """Select a taxi in range"""
    print("Taxi available:")
    display_all_taxi()
    option_number = int(input("Choose taxi: "))
    if 0 <= option_number < len(TAXIS):
        return TAXIS[option_number]
    else:
        print("Invalid taxi choice")
        return None


def display_all_taxi():
    """Display all taxis in the list"""
    for index_number, taxi in enumerate(TAXIS):
        print(f"{index_number} - {taxi}")


def drive_taxi(current_taxi):
    """Calculate vehicle travel distance based on input"""
    distance = int(input("Drive how far? "))
    current_taxi.drive(distance)
    current_taxi.get_fare()
    return current_taxi.get_fare()


main()
