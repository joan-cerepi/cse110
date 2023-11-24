"""
Purpose: Format strings and display them to the screen.
"""


def main() -> None:
    """The main function of the program."""
    first_name = input('What is your first name? ').title()
    last_name = input('What is your last name? ').title()
    print()
    print(f'Your name is {last_name}, {first_name} {last_name}.')


if __name__ == '__main__':
    main()
