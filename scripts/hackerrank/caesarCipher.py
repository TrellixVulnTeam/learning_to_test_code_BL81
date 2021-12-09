from typing import List
import string
"""
Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc
"""

class Solution:
    def caesarCipher(self, input_string, rotate):
        def findMatch(letter):
            if not letter.isalpha():
                return letter
            flag = bool(letter.isupper())
            alphabet = string.ascii_lowercase
            idx = (alphabet.find(letter.lower()) + rotate) % 26 
            return alphabet[idx].upper() if flag    else alphabet[idx].lower()
        return "".join(list(map(lambda l: findMatch(l), input_string)))

class Solution2:
    def caesarCipher(self, input_string, rotate):
        # Write your code here
        l = string.ascii_lowercase
        pos = {x:y for y,x in enumerate(l)}
        newString = []
        
        for i in input_string:
            toLowCase = i.lower()
            if toLowCase in l:
                newIndex = (pos[toLowCase] + rotate)%26
                newString.append(l[newIndex]) if i.islower() else newString.append(l[newIndex].upper())
            else:
                newString.append(i)
        
        return (''.join(newString))
    
    
if __name__ == "__main__":
    input_string = "There's a"    
    k = 3
    solution = Solution()
    print(solution.caesarCipher(input_string, k))

    solution_two = Solution2()
    print(solution_two.carsarCipher(input_string, k))