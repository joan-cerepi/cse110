"""
Purpose: Ask user for input using input().
"""


def main() -> None:
    """Main function of the program."""
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    END = "\033[0m"

    favorite_color = input('Please type your favorite color: ').lower().strip()
    print('Your favorite color is')
    match favorite_color:
        case 'black':
            print(f'{BLACK}{favorite_color}{END}')
        case 'red':
            print(f'{RED}{favorite_color}{END}')
        case 'green':
            print(f'{GREEN}{favorite_color}{END}')
        case 'brown':
            print(f'{BROWN}{favorite_color}{END}')
        case 'blue':
            print(f'{BLUE}{favorite_color}{END}')
        case 'purple':
            print(f'{PURPLE}{favorite_color}{END}')
        case 'cyan':
            print(f'{CYAN}{favorite_color}{END}')
        case 'light gray':
            print(f'{LIGHT_GRAY}{favorite_color}{END}')
        case 'dark gray':
            print(f'{DARK_GRAY}{favorite_color}{END}')
        case 'light red':
            print(f'{LIGHT_RED}{favorite_color}{END}')
        case 'light green':
            print(f'{LIGHT_GREEN}{favorite_color}{END}')
        case 'yellow':
            print(f'{YELLOW}{favorite_color}{END}')
        case 'light blue':
            print(f'{LIGHT_BLUE}{favorite_color}{END}')
        case 'light purple':
            print(f'{LIGHT_PURPLE}{favorite_color}{END}')
        case 'light cyan':
            print(f'{LIGHT_CYAN}{favorite_color}{END}')
        case 'light white':
            print(f'{LIGHT_WHITE}{favorite_color}{END}')
        case _:
            print(favorite_color)


if __name__ == '__main__':
    main()
