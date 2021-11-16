from scripts.hackerrank.swap_case import swap_case


class Test:
    test_cases = [
        ["Www.HackerRank.com", "wWW.hACKERrANK.COM"],
        ["Pythonist 2", "pYTHONIST 2"]  
    ]
    
    def test_swap_case(self):
        for case, expected in self.test_cases:
            assert expected == swap_case(case)