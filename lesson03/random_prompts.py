'''
Practice converting user input to numeric data types and perform calculations.
'''


def get_user_age() -> int:
    """Prompt the user for their age and return it."""
    while True:
        try:
            user_age = int(input('How old are you? '))
            return user_age
        except ValueError:
            print('You did not enter a valid age. Try again.\n')



def get_number_of_eggs() -> None:
    """Prompt the user for the number of eggs cartons they have and return the total number of eggs."""
    while True:
        try:
            num_of_cartons = int(input('How many egg cartons do you have? '))
            return num_of_cartons * 12
        except ValueError:
            print('You did not enter a valid number. Try again.\n')


def get_cookies_per_person() -> None:
    """Prompt the user for the number of cookies and number of people and return how many cookies are there per person."""
    while True:
        try:
            num_of_cookies = int(input('How many cookies do you have? '))
            num_of_people = int(input('How many people are there? '))
            return f'{num_of_cookies / num_of_people:.2f}'
        except ValueError:
            print('You did not enter a valid number. Try again.\n')


def main() -> None:
    """Main function of the program. This is where it all happens."""
    print('RANDOM PROMPTS\n')

    user_age = get_user_age()
    next_age = user_age + 1
    print(f'On your next birthday, you will be {next_age}.\n')

    num_of_eggs = get_number_of_eggs()
    print(f'You have {num_of_eggs} eggs.\n')

    cookies_per_person = get_cookies_per_person()
    print(f'Each person may have {cookies_per_person} cookies.')


if __name__ == '__main__':
    main()