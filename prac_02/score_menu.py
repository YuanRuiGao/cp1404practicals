MENU = ("(G)et a valid score (must be 0-100 inclusive)\n"
        "(P)rint result\n"
        "(S)how stars\n"
        "(Q)uit\n"
        ">---")
LOWEST_SCORE = 0
HIGHEST_SCORE = 100
BAD_SCORE = 50
PASSABLE_SCORE = 90


def main():
    """The main function for control flow"""
    score = -1
    choice = input(MENU).upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score("Enter score: ")
        elif choice == "P":
            if score == -1:
                print("please enter score first")
            else:
                message = get_feedback(score)
                print(message)
        elif choice == "S":
            if score == -1:
                print("please enter score first")
            else:
                print(score * "*")
        else:
            print("Invalid option")
        choice = input(MENU).upper()
    print("Bye")


def get_valid_score(prompt):
    """Make sure the score is within the selected range"""
    value = int(input(prompt))
    while value < LOWEST_SCORE or value > HIGHEST_SCORE:
        print("Invalid score")
        value = float(input("Enter score: "))
    return value


def get_feedback(score):
    """Determine the output based on the score"""
    if score < BAD_SCORE:
        return "Bad"
    if score < PASSABLE_SCORE:
        return "Passable"
    else:
        return "Excellent"


main()
