from scripts.hackerrank.fizzBuzz import fizzBuzz

class Test:
    test_cases = [
        [15, [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]]
    ]
    testable_functions = [fizzBuzz]

    def test_fizz_buzz(self):
        for f in self.testable_functions:
            for case, expected in self.test_cases:
                assert f(case) == expected

    