from scripts.tree_graph.pathSum import Solution
from scripts.tree_graph.populate_tree_with_null import Node, creatBTree, preorder_pythonic


class Test:
    test_trees = [
        # [test_tree, expected_preorder_tree]
        [[5,4,8,11,None,13,4,7,2,None,None,None,1], [5, 4, 11, 7, 2, 8, 13, 1, 4]]
    ]
    test_cases = [
        # [target, expected answer]
        [27, True], 
        [0, False]
    ]
    
    
    def test_pathSum(self):
        solution = Solution()
        for test_tree, expected_preorder_tree in self.test_trees:
            root = creatBTree(test_tree, 0)
            assert preorder_pythonic(root) == expected_preorder_tree
            
            for target, expected in self.test_cases:
                assert solution.hasPathSum(root, target) == expected