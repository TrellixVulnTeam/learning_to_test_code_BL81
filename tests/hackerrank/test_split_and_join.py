from scripts.hackerrank.split_and_join import split_and_join, split_and_join_two


class Test:
    test_cases = [
        ["this is a string", "this-is-a-string"],
        ["challenges make you better", "challenges-make-you-better"]
    ]
    testable_functions = [split_and_join, split_and_join_two]

    def test_split_and_join(self):
        for f in self.testable_functions:
            for case, expected in self.test_cases:
                assert f(case) == expected
    