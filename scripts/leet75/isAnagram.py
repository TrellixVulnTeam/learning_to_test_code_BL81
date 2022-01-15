


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s, t = sorted(s), sorted(t)
        dicts, dictt = {}, {}
        
        for l in s:
            dicts[l] = dicts.get(l, 0) + 1
        for l in t:
            dictt[l] = dictt.get(l, 0) + 1
        print(dicts)
        print(dictt)
        return dicts == dictt
        
        
if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    solution = Solution()
    print(solution.isAnagram(s, t))