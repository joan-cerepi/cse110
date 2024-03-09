'''
Assignment for practicing text input/output and formatting.
'''

import random
from madlibs import madlib


def main() -> None:
    """Main function of the program."""
    choice = random.choice([madlib.madlib_1, madlib.madlib_2])

    print('Please enter the following: ')
    print()
    choice()


if __name__ == '__main__':
    main()