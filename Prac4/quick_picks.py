"""
1404 Practical
"""

import random

minimum = 1
maximum = 45
numbers_per_line = 6


def main():
    number_quick_picks = int(input("How many quick picks? "))

    for i in range(number_quick_picks):
        quick_pick = []
        for o in range(numbers_per_line):
            number = random.randint(minimum, maximum)
            while number in quick_pick:
                number = random.randint(minimum, maximum)
            quick_pick.append(number)
        quick_pick.sort()
        # Took this line from the solution
        print(" ".join(f"{number:2}" for number in quick_pick))


main()
