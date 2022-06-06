# https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/discuss/1473993/Python-3-or-BFS-or-Explanation

# Explanation: try all possible variations and find the smallest one

import collections


class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        dq, visited = collections.deque([s]), set([s])
        ans, n = s, len(s)
        
        while dq:
            curr = dq.popleft()
            ans = min(ans, curr)   
            
            curr_a = "".join([
                str((int(curr[i]) + a) % 10) if i % 2 else curr[i] for i in range(n)
            ])
            curr_b = curr[b:] + curr[:b]
            if curr_a not in visited:
                dq.append(curr_a)
                visited.add(curr_a)
            if curr_b not in visited:
                dq.append(curr_b)
                visited.add(curr_b)
        return ans

if __name__ == '__main__':
    soln = Solution()
    print(soln.findLexSmallestString(s="5525", a=9, b=2))
