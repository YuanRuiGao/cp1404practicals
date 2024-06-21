HEX_COLOUR_CODE = {"absolute zero": "#0048ba", "acid green": "#b0bf1a", "aliceblue": "#f0f8ff",
                   "alizarin crimson": "#e32636", "amaranth": "#e52b50", "amber":  "#ffbf00",
                   "amethyst": "#9966cc", "antiqueWhite": "#faebd7", "apricot": "#fbceb1",
                   "aqua": "#00ffff"}

colour_name = input("Enter short state: ").lower()
while colour_name != "":
    try:
        print("Hex code is", HEX_COLOUR_CODE[colour_name])
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter short state: ").lower()
print("Thanks for using")
