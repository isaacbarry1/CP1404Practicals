"""
1404 Practical:
                Create a program that will allow
                the user to look up a hexadecimal
                colour code
"""

COLOUR_TO_CODE = {"AbsoluteZero": "0048ba", "AcidGreen": "b0bf1a",
                  "AliceBlue": "f0f8ff", "AlizarinCrimson": "e32636",
                  "Amaranth": "e52b50", "Amber": "ffbf00",
                  "Amethyst": "9966cc", "AntiqueWhite": "faebd7",
                  "Apricot": "fbceb1", "Aqua": "00ffff"}


colour = input("Please enter a colour: ")

while colour != " ":
    try:
        print("The code for", colour, "is, ", COLOUR_TO_CODE[colour])
    except KeyError:
        print("Invalid colour name.")
    colour = input("Please enter a colour: ")
