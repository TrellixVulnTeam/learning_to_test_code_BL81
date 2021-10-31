from copy import copy, deepcopy
from scripts.leet75.basic_binary_tree import Node, sample_tree

class Test:

    test_cases = [
        [Node(0), 0],
        [Node(1), 1]
    ]

    # returns root node of built-tree
    node0 = sample_tree()

    def test_node_str(self):
        node = Node(0)
        assert type(node.__str__()) == str
        assert node.__str__() == str(node.data)

    def test_sample_tree(self):
        assert [0, 2, 1] == [self.node0.data, self.node0.right.data, self.node0.left.data]

    def test_traversal_inorder(self):
        assert [3, 1, 4, 0, 5, 2, 6] == self.node0.traverse_inorder()