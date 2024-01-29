"""
Problem Statement:
Write a Python program to convert Celsius to Fahrenheit.
Conversion formula: Fahrenheit = (Celsius * 9/5) + 32
"""


def solution():
    celsius = float(input("Enter temarature in Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius} degrees C is {fahrenheit} degrees F")


if __name__ == "__main__":
    solution()
