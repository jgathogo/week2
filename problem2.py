import sys


def print_name_age_77():
    """
    Ask user their name and age. Print out their year of birth and year when they will be 77 years

    :return: name, age, year of birth and year when user will be 77 years old
    """
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    year_of_birth = 2021 - age
    year_77 = 2021 + (77 - age)

    print(f"Your name is {name} and you are {age} years old. Your were born in {year_of_birth}. You will be 77 years "
          f"in {year_77}")


def main():
    print_name_age_77()


if __name__ == "__main__":
    sys.exit(main())
