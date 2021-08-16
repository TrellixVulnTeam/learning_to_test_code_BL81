"""
Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.


extra_end('Hello') → 'lololo'
extra_end('ab') → 'ababab'
extra_end('Hi') → 'HiHiHi'
"""

input_string = "Hello"
end = input_string[-2:] * 3


def extra_end(input_string):
    return input_string[-2:] * 3

print(extra_end(input_string))