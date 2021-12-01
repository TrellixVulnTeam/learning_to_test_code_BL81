from scripts.hackerrank.findZigZagSequence import findZigZagSequence

test_cases = [
    ([2, 3, 5, 1, 4], [1, 2, 5, 4, 3]),
    ([2, 3, 5, 4, 1, 6, 7], [1, 2, 3, 7, 6, 5, 4])
]
testable_functions = [findZigZagSequence]

def test_findZigZagSequence():
    for f in testable_functions:
        for case, expected in test_cases:
            assert expected == f(case, len(case))

    