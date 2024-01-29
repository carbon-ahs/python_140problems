"""
Problem Statement:
Write a Python program to convert kilometers to miles
Conversion factor: 1 kilometer = 0.621371 miles
"""


def solution():
    CONVERTION_FACTOR = 0.621371
    kilomiters = float(input("KM? :"))
    miles = kilomiters * CONVERTION_FACTOR

    print(f"miles: {miles}")


if __name__ == "__main__":
    solution()
