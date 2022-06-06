from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # sourcery skip: remove-unnecessary-cast, simplify-constant-sum
        """
        -for a palindrome, its odd-count character has to be less than or equal to one.
        -then in order to get k many palindromic substrings, the number of odd-count characters has to be less than or equal to k
        -basically just getting frequency count of all the characters, then dividing by 2 and deducing how many palindromes we have by checking how many of the keys in the freq count are divisible by 2. palindromes have less than or equal to one odd-count character by definition.
        """
        if len(s) < k:
            return False
        
        freq = Counter(s)
        # return sum(1 for val in freq.values() if val % 2 != 0) <= k
        return len(list(filter(lambda x: x % 2 != 0, freq.values()))) <= k

if __name__ == '__main__':
    soln = Solution()
    print(soln.canConstruct(s="annabelle", k=2))

    assert soln.canConstruct(s="annabelle", k=2) == True
    assert soln.canConstruct("leetcode", 3) == False
    assert soln.canConstruct("true", 4) == True