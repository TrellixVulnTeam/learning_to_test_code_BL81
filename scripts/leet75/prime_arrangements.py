"""
LC 1175. Prime Arrangements [easy]

Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)

(Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a product of two positive integers both smaller than it.)

Since the answer may be large, return the answer modulo 10^9 + 7.

Example 1:

Input: n = 5
Output: 12
Explanation: For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the prime number 5 is at index 1.

Example 2:

Input: n = 100
Output: 682289015
"""
from typing import List, Optional
from itertools import permutations


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        """Got this to pass time limit...now exceeds memory limit..good progress :)"""
        l = list(range(1, n+1))
        perms = list(permutations(l))
        count = 0

        for perm in perms:
            flag = True
            for i in range(len(perm)):
                if self.isprime(perm[i]) and not self.isprime(i+1):
                        flag = False
                        break
            if flag:
                count += 1
            print(count)

        return int(count % (1e9 + 7))

    def isprime(self, num: int) -> bool:
        if num <= 1:
            return False

        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    # return True if num == 1 else all(num % i != 0 for i in range(2, num))

if __name__ == '__main__':
    n = 5
    soln = Solution()
    assert soln.isprime(n) == True
    assert soln.isprime(1) == False
    assert soln.isprime(4) == False
    assert soln.isprime(6) == False
    assert soln.isprime(0) == False

    print(soln.numPrimeArrangements(n))
    # print(permutations(list(range(1, n + 1))))
    # print(list(range(1, n+1)))