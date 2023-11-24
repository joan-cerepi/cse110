"""
Purpose: Team Activity about formatting text in Python.
"""


def formatter(func):
    """Decorator for ID badge.

    Parameters
        func: function to be decorated.
    Return
        function"""
    def wrapper() -> None:
        print('-' * 64)
        func()
        print('-' * 64)
    return wrapper


def main() -> None:
    """Main function of the program."""
    print('Please enter the following information:')
    print()
    first_name = input('First name: ')
    last_name = input('Last name: ').upper()
    email = input('Email address: ').lower()
    phone = input('Phone number: ')
    job_title = input('What is your job title? ').title()
    id = input('ID Number: ')
    hair_color = input('Hair color: ').title()
    eye_color = input('Eye color: ').title()
    month_started = input('Month started: ').capitalize()
    training = input('Training (yes/no): ').capitalize()
    print()
    print('The ID Card is:')

    @formatter
    def display_badge() -> None:
        """Display neatly formatted badge."""
        print(f'{last_name}, {first_name}')
        print(f'{job_title}')
        print(f'{id}')
        print()
        print(f'{email}')
        print(f'{phone}')
        print()
        print(f'Hair: {hair_color:20} Eyes: {eye_color}')
        print(f'Month: {month_started:17} Training: {training}')

    display_badge()


if __name__ == '__main__':
    main()
