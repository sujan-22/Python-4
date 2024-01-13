#I Sujan Rokad, 000882948, certify that this work is my own effort and that I have not allowed anyone to copy from it.

"""
Author:                 Sujan Rokad
Authorship statement:   I, Sujan Rokad, 000882948, certify that this material is my original work. No other person's work has been used without due acknowledgement.
Purpose:                Print prime numbers up to a given number.
"""

def prime_num(number):
    """
    Prints prime numbers up to a given number.

    Args:
        number (int): The upper limit for finding prime numbers.
    """
    primes = [True] * (number + 1)

    for n in range(2, int(number**0.5) + 1):
        if primes[n]:
            for i in range(n * 2, number + 1, n):
                primes[i] = False

    print("Prime numbers up to", number, "are:")
    for n in range(2, number + 1):
        if primes[n]:
            print(n, end=" ")


# Get user input for the number
number = int(input("Enter a Number which is greater than or equal to 100: "))
prime_num(number)
