from scripts.interview_questions_notion.iterative_string_perms import iterative_string_perms


class Test:
    test_cases = [
        ("abc", ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']), 
        ("cat", ['cat', 'act', 'atc', 'cta', 'tca', 'tac']), 
        ("dog", ['dog', 'odg', 'ogd', 'dgo', 'gdo', 'god'])
    ]
    testable_functions = [iterative_string_perms]

    def test_iterative_string_perms(self):
        for f in self.testable_functions:
            for case, expected in self.test_cases:
                assert f(case) == expected

    