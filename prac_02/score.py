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
