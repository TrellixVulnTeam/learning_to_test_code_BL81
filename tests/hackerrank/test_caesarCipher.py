from scripts.hackerrank.caesarCipher import Solution, Solution2


class Test:
    test_cases = [
        [["middle-Outz", 2], "okffng-Qwvb"]
    ]
    testable_objects = [Solution, Solution2]
    
    def test_caesar_cipher_solution1(self):
        for obj in self.testable_objects:
            obj = obj()
            for case, expected in self.test_cases:
                assert expected == obj.caesarCipher(case[0], case[1])