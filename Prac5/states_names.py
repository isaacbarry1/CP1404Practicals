"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""


import pprint

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales",
                "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria",
                "TAS": "Tasmania"}

# Prints all the states with state codes
for key, value in CODE_TO_NAME.items():
    print(key, " : ", value)


state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(state_code, "is", CODE_TO_NAME[state_code])
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ")



