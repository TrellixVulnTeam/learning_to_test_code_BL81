
"""
Given a string, return a new string where the first and last chars have been exchanged.


front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'
"""


##################### Python strings are immutable!! #################
# cant do this with strings
# some_string[0] = "k" # error!!!


def front_back(str):
    # turn string into list and get first and last characters
    liststring = list(str)
    newfront,  newback = liststring[-1], liststring[0]

    # reassign
    liststring[0] = newfront
    liststring[-1] = newback

    return "".join(i for i in liststring)

print(front_back("code"))

def front_back_refactor1(str):
    if len(str) <= 1:
        return str
    
    # this is a string
    mid = str[1:len(str) - 1] # can be written as str[1:-1]

    # last + mid + first
    return str[len(str) - 1] + mid + str[0]

print(front_back_refactor1("code"))