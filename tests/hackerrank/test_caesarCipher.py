from scripts.hackerrank.caesarCipher import caesarCipher


class Test:
    test_cases = [
        [["middle-Outz", 2], "okffng-Qwvb"]
    ]
    testable_functions = [caesarCipher]
    
    def test_caesar_cipher(self):
        for f in self.testable_functions:
            for case, expected in self.test_cases:
                assert expected == f(case[0], case[1])