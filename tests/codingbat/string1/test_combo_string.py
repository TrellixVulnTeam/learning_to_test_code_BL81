from scripts.codingbat.string1.combo_string import (
        combo_string,   
        combo_string_refactor, 
        combo_string_refactor_2
    )

class Test:
    test_cases = [
        (("Hello", "hi"), "hiHellohi"),
        (("kevin", "zehnder"), "kevinzehnderkevin")
    ]
    testable_functions = [
        combo_string, combo_string_refactor, combo_string_refactor_2
    ]

    def test_combo_string(self):
        for f in self.testable_functions:
            for [case, expected] in self.test_cases:
                assert f(case[0], case[1]) == expected