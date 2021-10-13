from collections import Counter

def palindromeRearranging(inputString):
    return sum(i % 2 == 1 for i in Counter(inputString).values()) <= 1

def is_palindrome_permutation_pythonic(phrase):
    """function checks if a string is a permutation of a palindrome or not"""
    counter = Counter(phrase.replace(" ", "").lower())
    return sum(val % 2 for val in counter.values()) <= 1

# NOTE: basically, palindrome in wrong order?