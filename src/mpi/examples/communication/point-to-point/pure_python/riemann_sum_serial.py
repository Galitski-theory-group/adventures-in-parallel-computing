"""
This program dynamically creates a single-line function from user input,
then calculates the approximate integral of this function over a specified
interval using the left Riemann sum method.

The program consists of the following functions:

1. is_single_line(expression: str) -> bool:
    - Checks if a given string expression is a single line.

2. create_function_from_user_input() -> Callable:
    - Prompts the user to enter a single-line function body and dynamically creates
    this function.

3. riemann_sum_left(f: Callable[[float], float], interval: tuple, n: int) -> float:
    - Approximates the integral of a function on a given interval using the left
    Riemann sum.

4. main():
    - Main function to execute the program. It creates a user-defined function, takes
    interval and partition number inputs, and calculates the integral using the left
    Riemann sum method.

Usage:
- Run the program.
- Enter a single-lined function body when prompted.
- Enter the start and end of the interval and the number of partitions when prompted.
- The program will output the approximate integral of the function over the specified
 interval.
"""

from typing import Callable


def is_single_line(expression: str) -> bool:
    """
    Takes a string expression and checks if the string is one-line by counting
    /n (newline) characters.

    Parameters:
    - expression: the function body in string form

    Returns:
    A boolean indicating if function body is single-lined (true)

    """
    # Count the number of newline characters
    newline_count = expression.count("\n")
    # Return True if there is only one newline character, False otherwise
    return newline_count == 0


def create_function_from_user_input() -> Callable:
    """
    Dynamically create a single-lined function from user input.

    Parameters:

    Returns:
    A single-lined function of form f(x): return expression
    """
    locals_dict = {}
    # Get a string from the user
    function_string = input("Enter a single-lined function body: ")
    # Check that string is well-formed
    assert is_single_line(function_string)
    # Execute code while making sure that scope of f is not just in exec bloc
    exec(f"def f(x): return {function_string}", {}, locals_dict)
    return locals_dict["f"]


def riemann_sum_left(
    f: Callable[[float, int], float], interval: tuple, n: int
) -> float | int:
    """
    Takes function f, an interval (a,b) defined as a tuple, and a partition number n
    and approximates the integral of f on [a,b]

    Parameters:
    - f: function
    - interval: interval (a,b) where b>a
    - n : partition number, how many rectangles to approximate integral

    Returns:
    integral, the result of integration process, "area under the curve".

    Example:
    """

    assert interval[1] > interval[0]

    delta_x = (interval[1] - interval[0]) / n
    x = [interval[0] + i * delta_x for i in range(0, n)]
    sum = 0
    for i in range(0, n):
        sum += f(x[i]) * delta_x
    return sum


def main():
    f = create_function_from_user_input()

    assert callable(f)

    a, b, n = input(
        """Enter start of interval,\
 end of interval, and partition number: """
    ).split()

    print(a, b, n)
    # type convert into appropriate format
    a, b = tuple(map(float, [a, b]))
    n = int(n)

    assert a < b

    result = riemann_sum_left(f, (a, b), n)
    print(f"The integral of {f} on [{a},{b}] given n={n}:\n result: {result}\n")


if __name__ == "__main__":
    main()
