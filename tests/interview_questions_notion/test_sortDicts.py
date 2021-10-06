from scripts.interview_questions_notion.sortDicts import sort_dict_by_value_looping, refactor_sort_dict_by_looping, sort_dict_by_value_pythonic

class Test:
    test_cases = [
        ({1: 1, 2: 9, 3: 4}, {1: 1, 3: 4, 2: 9}),
        ({2: 10, 3: 0, 1: 1}, {3: 0, 1: 1, 2: 10}),
    ]
    testable_functions = [
        sort_dict_by_value_looping, 
        refactor_sort_dict_by_looping, 
        sort_dict_by_value_pythonic]

    def test_sort_dict_by_value_looping(self):
        for f in self.testable_functions:
            for [test_string, expected] in self.test_cases:
                assert f(test_string) == expected