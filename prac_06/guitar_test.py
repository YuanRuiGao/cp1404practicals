from prac_06.guitar import Guitar
guitars = [
    Guitar("Gibson L-5 CES", 1922, 16035.40),
    Guitar("Another Guitar", 2013, 0)
]

print(f"Gibson L-5 CES get_age() - Expected 100. Got {guitars[0].get_age()}")
print(f"Another Guitar get_age() - Expected 9. Got {guitars[1].get_age()}")
print(f"Gibson L-5 CES is_vintage() - Expected True. Got {guitars[0].is_vintage()}")
print(f"Another Guitar is_vintage() - Expected False. Got {guitars[1].is_vintage()}")
