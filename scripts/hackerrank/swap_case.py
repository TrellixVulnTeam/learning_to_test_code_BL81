"""
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2  
"""

def swap_case(input_string):
    output = ""
    for character in input_string:
        if character.isalpha():
            if character.isupper():
                output += character.lower()
            else:
                output += character.upper()
        else:
            output += character
    return output

if __name__ == "__main__":
    input_string = "Www.HackerRank.com"
    print(swap_case(input_string))