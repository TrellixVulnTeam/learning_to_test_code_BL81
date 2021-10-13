from scripts.interview_questions_notion.binary_search_tree import (
    Node,
    BinarySearchTree
)
"""
    Example
                  8
                 / \
                3   10
               / \    \
              1   6    14
                 / \   /
                4   7 13
    >>> t = BinarySearchTree().insert(8, 3, 6, 1, 10, 14, 13, 4, 7)
    >>> print(" ".join(repr(i.value) for i in t.traversal_tree()))
    8 3 1 6 4 7 10 14 13
"""

class Test:

    def test_node(self):
        node = Node(100, None)
        assert node.value == 100
        assert node.parent == None
        assert node.left == None
        assert node.right == None

    def test_binary_search_tree(self):
        bst = BinarySearchTree()
        bst.insert(8, 3, 6, 1, 10, 14, 13, 4, 7)
        assert " ".join(repr(i.value) for i in bst.traversal_tree()) == "8 3 1 6 4 7 10 14 13"

