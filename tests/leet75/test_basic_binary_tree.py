from copy import copy, deepcopy
from scripts.leet75.basic_binary_tree import create_tree, inorder, inorder_pythonic, depth_of_tree


class Test:

    test_cases = [
        [],
        []
    ]

    def test_create_tree(self):
        tree = create_tree()
        assert 0 == tree.data
        assert 1 == tree.left.data
        assert 2 == tree.right.data

    def test_inorder(self):
        tree = create_tree()
        inorder(tree)

    def test_inorder_pythonic(self):
        tree = create_tree()
        assert [1, 0, 2] == inorder_pythonic(tree)

    def test_is_full(self):
        pass

    def test_depth_of_tree(self):
        tree = create_tree()
        assert 2 == depth_of_tree(tree)