import random

LOWEST_SCORE = 0
HIGHEST_SCORE = 100
BAD_SCORE = 50
PASSABLE_SCORE = 90


def main():
    """The main function for control flow, then get a random score and execute get_feedback"""
    score = float(input("Enter score: "))
    while score < LOWEST_SCORE or score > HIGHEST_SCORE:
        print("Invalid score")
        score = float(input("Enter score: "))
    massage = get_feedback(score)
    print(massage)

    score = random.randint(LOWEST_SCORE, HIGHEST_SCORE)
    massage = get_feedback(score)
    print(massage)


def get_feedback(score):
    """Determine the output based on the score"""
    if score < BAD_SCORE:
        return "Bad"
    if score < PASSABLE_SCORE:
        return "Passable"
    else:
        return "Excellent"


main()
