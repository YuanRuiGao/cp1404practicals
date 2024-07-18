from prac_07.guitar import Guitar
from operator import itemgetter

guitars = []
with open("guitars.csv", "r") as guitars_information:
    for line in guitars_information:
        parts = line.strip().split(",")
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
guitars.sort()

for i in guitars:
    print(i.name, i.year, i.cost)
