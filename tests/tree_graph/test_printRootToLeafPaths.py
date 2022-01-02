from scripts.tree_graph.printRootToLeafPaths import Node, preorder_pythonic, binaryTreeRootToLeafPythonic, binaryTreeRootToLeafRecursive, binaryTreeRootToLeafIterative


class Test:
    test_cases = []
    
    def test_node(self):
        root = Node(0)
        root.left = Node(1)
        root.right = Node(2)
        root.left.left = Node(3)
        root.left.right = Node(4)
        assert preorder_pythonic(root) == [0, 1, 3, 4, 2]

    def binaryTreeRootToLeafRecursive(self):
        root = Node(0)
        root.left = Node(1)
        root.right = Node(2)
        root.left.left = Node(3)
        root.left.right = Node(4)
    
        test_case = [root, ['0->1->3', '0->1->4', '0->2']]
        assert binaryTreeRootToLeafRecursive(test_case[0]) == test_case[1]

    def test_binaryTreeRootToLeafPythonic(self):
        root = Node(0)
        root.left = Node(1)
        root.right = Node(2)
        root.left.left = Node(3)
        root.left.right = Node(4)
    
        test_case = [root, ['0->1->3', '0->1->4', '0->2']]
        test_case[1].reverse()
        
        assert binaryTreeRootToLeafPythonic(test_case[0]) == test_case[1]
        

    def binaryTreeRootToLeafIterative(self):
        root = Node(0)
        root.left = Node(1)
        root.right = Node(2)
        root.left.left = Node(3)
        root.left.right = Node(4)
    
        test_case = [root, ['0->1->3', '0->1->4', '0->2']]
        assert binaryTreeRootToLeafIterative(test_case[0]) == test_case[1]