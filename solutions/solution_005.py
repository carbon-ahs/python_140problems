"""
Problem Statement:
Write a Python program to generate a random number.
"""
import random


def solution():
    upper_limit = 100
    lower_limit = 0
    print(
        f"Here ni a random number bettwen upper and lower limit: {random.randint(lower_limit, upper_limit)}"
    )


if __name__ == "__main__":
    solution()
