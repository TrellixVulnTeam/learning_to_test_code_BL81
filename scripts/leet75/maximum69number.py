"""
1323. Maximum 69 Number [Easy]

Share
You are given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

Example 1:

Input: num = 9669
Output: 9969
Explanation: 
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.
Example 2:

Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.
Example 3:

Input: num = 9999
Output: 9999
Explanation: It is better not to apply any change.
"""

class Solution:
    def maximum69Number (self, num: int) -> int: 
        if all([s == str(9) for s in str(num)]):
            print(num)
            return num

        num_as_string = "".join(str(num))
        num_as_list = list(num_as_string)

        poss = []
        for i in range(len(num_as_string)):
            tmp = num_as_list[:]

            if tmp[i] == str(9):
                tmp[i] = str(6)
            elif tmp[i] == str(6):
                tmp[i] = str(9)
        
            poss.append(tmp)
        
        print(poss)
        poss_as_int = [list(map(int, ele)) for ele in poss]
        # poss_sum = list(map(lambda x: "".join(x), poss_as_int))
        print(poss_as_int)
        output = []
        for p in poss_as_int:
            joined = [str(i) for i in p]
            res = int("".join(joined))
            output.append(res)
        print(max(output))
        return(max(output))


if __name__ == '__main__':
    # num = 9669
    num = 99

    soln = Solution()
    soln.maximum69Number(num)