"""
Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".


first_half('WooHoo') → 'Woo'
first_half('HelloThere') → 'Hello'
first_half('abcdef') → 'abc'
"""

input_string = "WooHoo"
middle = len(input_string) // 2
first_half = input_string[:middle]
print(first_half)

def first_half(str):
    middle = len(str) // 2
    return str[:middle]


print(first_half(input_string))