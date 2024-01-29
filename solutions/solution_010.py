"""
Problem Statement:
Write a Python program to swap two variables without temp variable.
"""


def solution():
    a = 11
    b = 22
    a, b = b, a
    print(f"a: {a} b:{b}")
    pass


if __name__ == "__main__":
    solution()
