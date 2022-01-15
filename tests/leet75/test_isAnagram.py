from scripts.leet75.isAnagram import Solution


class Test:
    
    test_cases = [
        ["anagram", "nagaram", True],
        ["car", "rat", False]
    ]
    
    
    def test_isAnagram(self):
        solution = Solution()
        for s1, s2, expected in self.test_cases:
            assert solution.isAnagram(s1, s2) == expected