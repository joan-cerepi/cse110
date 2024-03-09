'''
Purpose: Use variables to solve a problem.
'''

import math
import pyfiglet


def display_banner(text: str, font: str = 'slant') -> None:
    """Display ASCII art banner using the pyfiglet library.

    Parameters
        text: text you want to be displayed.
        font: art font of the text to be displayed.
    Return
        rtype: None.

    Font options

    """
    banner = pyfiglet.figlet_format(text, font)
    print(banner)
    print()


def value_getter() -> float:
    """Check value and make sure that it's a number."""
    while True:
        try:
            value = float(
                input('Enter value: ')
            )
            return value
        except ValueError:
            print('Value needs to be a number.')
            print()


def calculate_square_area() -> float:
    """Function that calculates the area of a square."""
    side_length = value_getter()
    return side_length * side_length


def calculate_rect_area() -> float:
    """Function that calculates the area of a rectangle."""
    length = value_getter()
    width = value_getter()
    return length * width


def calculate_circle_area() -> float:
    """Function that calculates the area of a circle."""
    radius = value_getter()
    return f'{math.pi * (radius ** 2):.2f}'


def main() -> None:
    display_banner('Shape Area Calculator')

    print('What is the length of a side of the square?')
    square_area = calculate_square_area()
    print(f'The area of the square is: {square_area}')
    print()

    print('What are the length and width of the rectangle?')
    rect_area = calculate_rect_area()
    print(f'The area of the rectangle is: {rect_area}')
    print()

    print('What is the area of the circle?')
    circle_area = calculate_circle_area()
    print(f'The area of the circle is: {circle_area}')
    

if __name__ == '__main__':
    main()