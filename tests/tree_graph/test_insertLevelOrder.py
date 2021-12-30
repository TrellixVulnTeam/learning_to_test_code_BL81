from scripts.tree_graph.insertLevelOrder import insertLevelOrder, inorder_pythonic, Node



class Test:
    # expected 0 traversal type: preorder
    test_cases = [
        [[5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], [5, 4, 11, 7, 2, 8, 13, 4, 1]]
    ]
    testable_functions = [insertLevelOrder]
    
    def test_insertLevelOrder(self):
        root = None
        for f in self.testable_functions:
            for case, expected in self.test_cases:
                assert f(case, root, 0, len(case)) == expected
                
    def test_traverseInorder(self):
        root = None
        for case, expected in self.test_cases:
            res = insertLevelOrder(case, root, 0, len(case))
            assert inorder_pythonic(res) == expected
                
    def test_inorder_pythonic(self):
        root = Node(0)
        root.left = Node(1)
        root.right = Node(2)
        assert inorder_pythonic(root) == [1, 0, 2]