from scripts.interview_questions_notion.recursive_fib import fib_recur

class Test:
    test_cases = [
        (3, 2),
        (4, 3),
        (5, 5)
    ]
    testable_functions = [fib_recur]

    def test_recursive_fibonacci(self):
        for f in self.testable_functions:
            for case, expected in self.test_cases:
                assert f(case) == expected
    