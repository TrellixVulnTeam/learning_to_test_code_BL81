"""
Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.


without_end('Hello') → 'ell'
without_end('java') → 'av'
without_end('coding') → 'odin'
"""

input_string = "Hello"
trimmed = input_string[1:-1]
print(trimmed)

def without_end(str):
    return str[1:-1]

print(without_end(input_string))