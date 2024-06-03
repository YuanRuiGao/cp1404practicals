"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

LOWEST_SCORE = 0
HIGHEST_SCORE = 100
BAD_SCORE = 50
PASSABLE_SCORE = 90

score = float(input("Enter score: "))

# if score < 0:
#     print("Invalid score")
# else:
#     if score > 100:
#         print("Invalid score")
#     if score > 50:
#         print("Passable")
#     if score > 90:
#         print("Excellent")
# if score < 50:
#     print("Bad")

if score < LOWEST_SCORE or score > HIGHEST_SCORE:
    print("Invalid score")
elif score < BAD_SCORE:
    print("Bad")
elif score < PASSABLE_SCORE:
    print("Passable")
else:
    print("Excellent")

import random

LOWEST_SCORE = 0
HIGHEST_SCORE = 100
BAD_SCORE = 50
PASSABLE_SCORE = 90


def main():
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
    if score < BAD_SCORE:
        return "Bad"
    if score < PASSABLE_SCORE:
        return "Passable"
    else:
        return "Excellent"


main()
