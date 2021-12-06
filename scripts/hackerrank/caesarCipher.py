from typing import List
import string

def caesarCipher(s: str, k: int) -> str:
    pass

def rotate(alphabet: str, rotate: int) -> str:
    alphabet = alphabet[rotate:] + alphabet[:rotate]
    return alphabet

"""
Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc
"""
if __name__ == "__main__":
    input_string = "There's a"    
    alphabet = ""
    for letter in string.ascii_lowercase:
        alphabet += letter
    print(f'Original alphabet:\n{alphabet}')
    
    new_alphabet = rotate(alphabet, 3)
    output = ""
    for letter in input_string:
        if letter.isalpha():
            original_index = alphabet.find(letter.lower())
            output += new_alphabet[original_index].upper() if letter.isupper() else new_alphabet[original_index].lower()
            print(alphabet[original_index], "-->", new_alphabet[original_index].upper() if letter.isupper() else new_alphabet[original_index].lower())
        else:
            output += letter
            print(letter)
    print(f'output: {output}')