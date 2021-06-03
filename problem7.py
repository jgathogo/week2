import os
import sys


def main():
    line_1 = "apache license".center(50, " ")
    line_2 = "version 2.0, january 2004".center(50, " ")
    line_3 = "http://www.apache.org/licenses/".center(50, " ")
    print(line_1.title())
    print(line_2.title())
    print(line_3.title())

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
