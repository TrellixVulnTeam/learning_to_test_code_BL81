from scripts.leet75.node import Node

class Test:
    
    test_cases = [
        [4, 4],
        [0, 0]
    ]
    testable_functions = []

    def test_node(self):
        for case, expected in self.test_cases:
            new_node = Node(case)
            assert expected == new_node.data
