import os
import sys


def print_name_age():
    """
    Ask user name and age and print out the result

    :return: name and age entered
    """
    name = input("Please enter your name: ")
    age = input("Please enter your age in years: ")
    print(f"Your name is {name} and you are {age} years old")


def main():
    print_name_age()
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
