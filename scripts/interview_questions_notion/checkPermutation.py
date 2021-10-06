# O(N)
import unittest
from collections import Counter


def check_permutation_by_sort(s1, s2):
    if len(s1) != len(s2):
        return False
    s1, s2 = sorted(s1), sorted(s2)
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True

def check_permutation_pythonic(str1, str2):
    if len(str1) != len(str2):
        return False

    return Counter(str1) == Counter(str2)