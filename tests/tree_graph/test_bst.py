from scripts.tree_graph.bst import Node, deleteNode, preorder, inorder, preorder_verbose, insert, minValueNode, deleteNode, tree_build



class Test:
    
    test_cases = []
    
    def test_tree_build(self):
        expected_preorder = [8, 3, 1, 6, 4, 10]
        root = tree_build()
        assert preorder(root) == expected_preorder
        
    def test_insertNode(self):
        expected_preorder = [8, 3, 1, 6, 4, 10, 14]
        root = tree_build()
        root = insert(root, 14)
        assert preorder(root) == expected_preorder

    def test_deleteNode(self):
        expected_preorder = [8, 3, 1, 6, 4]
        root = tree_build()
        root = deleteNode(root, 10)
        assert preorder(root) == expected_preorder