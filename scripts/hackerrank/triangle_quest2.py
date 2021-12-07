# see:
# https://www.hackerrank.com/challenges/triangle-quest-2/forum

"""
Explanation:

Demlo numbers
The output requires the sequence of Demlo numbers. For n<=9, the squares of the first few repunits are precisely the Demlo numbers. Example: 1^2=1, 11^2=121, 111^2=12321 and so on.

At first lets see how to get repunits. (10^i - 1) / 9 results in the repunits sequence: 1, 11, 111 etc.

Then calculating square of each repunits, we can get Demlo numbers.

So, the code to perform these operations to generate Demlo numbers is:

for i in range(1,int(raw_input())+1): 
    print(((10**i)/9)**2)
"""

"""
Note: This is my solution that "sort of" works but doesn't satisfy the constraints of the problem (namely, it uses string methods which question says you are not allowed to use)

sample_input = 5
for i in range(1, int(sample_input) + 1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    forwards = [i for i in range(1, i+1)]
    print([i for i in forwards] + [i for i in sorted(forwards[:-1], reverse=True)], end="")
    print(" ")
"""
   

for i in range(1,int(input())+1):
     print((10**i//9)**2)