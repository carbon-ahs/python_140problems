"""
Problem Statement:
Write a Python program to display calendar.
"""
import calendar


def solution():
    year = 2023
    month = 11

    calender = calendar.month(year, month)
    print(calender)


if __name__ == "__main__":
    solution()
