"""
Problem Statement:
Write a Python program to swap two variables.
"""


def solution():
    a = 11
    b = 22
    temp = a
    a = b
    b = temp

    print(f"a: {a} b:{b}")


if __name__ == "__main__":
    solution()
