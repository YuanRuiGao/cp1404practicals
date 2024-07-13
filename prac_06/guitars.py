from prac_06.guitar import Guitar
print("My guitars!")

guitars = [
    Guitar("Gibson L-5 CES", 1922, 16035.40),
    Guitar("Another Guitar", 2013, 11512.9)
]
guitar_name = input("Name: ")
while guitar_name != "":
    guitar_year = int(input("Year: "))
    guitar_cost = int(input("Cost: "))
    print(f"{guitar_name} ({guitar_year}) : ${guitar_cost:,.2f} added.\n")
    guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))
    guitar_name = input("Name: ")
print("\n... snip ...\nThese are my guitars:")
guitar_number = 0
length_of_name = max([len(guitar.name) for guitar in guitars])
length_of_year = max([len(str(guitar.year)) for guitar in guitars])
length_of_cost = max([len(str(f"{guitar.cost:,.2f}")) for guitar in guitars])
for guitar in guitars:
    guitar_number += 1
    vintage_string = ""
    if guitar.is_vintage():
        vintage_string = "(vintage)"
    print(f"Guitar {guitar_number}: {guitar.name:>{length_of_name}} ({guitar.year:>{length_of_year}}), worth $"
          f" {guitar.cost:{length_of_cost},.2f}{vintage_string}")

