from scripts.tree_graph.binary_tree_traversals import Node, preorder, inorder, createBTree, level_order


class Test:
    test_cases = [
        # [data, preorder, inorder]
        [[0, 1 ,2, 3, 4, 5, None],
         [0, 1, 3, 4, 2, 5],
         [3, 1, 4, 0, 5, 2]]
    ]
    
    def test_build_tree(self):
        for data, expected_preorder, expected_inorder in self.test_cases:
            root = createBTree(data, 0)
            assert preorder(root) == expected_preorder
            assert inorder(root) == expected_inorder
           
    def test_level_order_bfs_traversal(self):
        expected = [0, 1, 2, 3, 4, 5]
        root = createBTree(self.test_cases[0][0], 0)
        assert level_order(root) == expected
            

            
            
