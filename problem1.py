import os
import sys

"""
Notes: 
- It's great that you've used functions even though we haven't reached that part of the course. 
Also, the naming of the function is clear and a good variable name.
- Typically, the docstring for the function starts immediately after the triple quote otherwise we 
introduce a newline (\n) in the documentation, which doesn't look good. I've corrected it below.
- The 'return' variable in the docstring is not correct since your program actually returns None (you can test this)
"""

def print_name_age():
    """Ask user name and age and print out the result

    :return: None
    """
    name = input("Please enter your name: ")
    age = input("Please enter your age in years: ")
    print(f"Your name is {name} and you are {age} years old")


def main():
    v = print_name_age()
    print(f"the return value of 'print_name_age()' is {v}")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
