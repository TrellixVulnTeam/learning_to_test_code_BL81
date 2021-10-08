from scripts.codingbat.string1.left2 import (
    left2, 
    left2_refactor
)

class Test:
    test_cases = [
        [("Hello", 2), "lloHe"],
        [("pythonprogram", 2), "thonprogrampy"]
    ]
    testable_functions = [left2, left2_refactor]

    def test_string_rotation(self):
        for f in self.testable_functions:
            for case, expected in self.test_cases:
                assert f(*case) == expected