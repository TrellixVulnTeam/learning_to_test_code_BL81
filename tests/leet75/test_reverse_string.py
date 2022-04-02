from scripts.leet75.reverse_string import Solution


class Test:

    test_cases = [
        [["h", "e", "l", "l", "o"], ["o","l","l","e","h"]],
        [["H","a","n","n","a","h"], ["h","a","n","n","a","H"]]
    ]

    def test_reverse_string(self):
        soln = Solution()

        for case, expected in self.test_cases:
            assert soln.reverseString(case) == expected


if __name__ == '__main__':
    soln = Solution()
    inp1 = ["h", "e", "l", "l", "o"]

    print(soln.reverseString(inp1))