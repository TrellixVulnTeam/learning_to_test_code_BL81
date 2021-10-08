from scripts.codingbat.string1.hello_name import hello_name


class Test:
    test_cases = [
        ("Bob", "Hello Bob!"),
        ("X", "Hello X!"),
        ("Kevin", "Hello Kevin!"),
    ]
    testable_functions = [hello_name]

    def test_hello_name(self):
        for f in self.testable_functions:
            for case, expected in self.test_cases:
                assert f(case) == expected