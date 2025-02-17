# ANSI Colors.
BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
YELLOW = "\033[1;33m"
END = "\033[0m"


def print_color(color: str) -> None:
    """Check color, make sure output color matches name of color and print value."""
    suffix = f'{color.title()}{END}'

    match color:
        case 'black':
            print(BLACK + suffix)
        case 'red':
            print(RED + suffix)
        case 'green':
            print(GREEN + suffix)
        case 'brown':
            print(BROWN + suffix)
        case 'blue':
            print(BLUE + suffix)
        case 'purple':
            print(PURPLE + suffix)
        case 'cyan':
            print(CYAN + suffix)
        case 'yellow':
            print(YELLOW + suffix)
        case _:
            print(suffix)


def main() -> None:
    """Main function of the program."""
    fav_color = input('Please type your favorite color: ')
    fav_color_clean = fav_color.lower().strip()
    print('Your favorite color is')
    print_color(fav_color_clean)


if __name__ == '__main__':
    main()