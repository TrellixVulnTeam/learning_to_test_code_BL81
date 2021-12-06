from scripts.hackerrank.print_function import print_function, print_function_with_string_methods


class Test:
    
    test_cases = [
        ["3", "123"],
        ["5", "12345"]
    ]
    testable_functions = [print_function, print_function_with_string_methods]
    
    def test_print_function(self):
        for f in self.testable_functions:
            for case, expected in self.test_cases:
                assert expected == f(case)
    