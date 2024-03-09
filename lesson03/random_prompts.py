'''
Checkpoint assignment.
Practice using mathematical expressions.
'''


def value_getter() -> int:
    """Keep prompting user for value if value not numeric."""
    while True:
        try:
            numeric_value = int(
                input('Enter value: ')
            )
            return numeric_value
        except ValueError:
            print("You didn't enter a number. Try again!")
            print()



def main() -> None:
    """Main function of the program."""
    print('How old are you?')
    current_age = value_getter()
    next_year_age = current_age + 1
    print(f'On your next birthday, you will be {next_year_age}.')
    print()

    print('How many egg cartons do you have?')
    num_of_cartons = value_getter()
    num_of_eggs = num_of_cartons * 12
    print(f'You have {num_of_eggs} eggs')
    print()

    print('How many cookies do you have?')
    num_of_cookies = value_getter()
    print('How many people are there?')
    num_of_people = value_getter()
    print(f'Each person may have {num_of_cookies / num_of_people:.2f} cookies')


if __name__ == '__main__':
    main()