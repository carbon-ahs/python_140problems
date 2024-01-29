"""
Problem Statement:
Write a Python Program to Check Leap Year.
"""


def solution():
    year = 1300

    if year % 100 == 0 and year % 400 == 0:
        print("Leap Year!")
    elif year % 100 != 0 and year % 4 == 0:
        print("Leap Year!")
    else:
        print("Not Leap Year!")


if __name__ == "__main__":
    solution()
