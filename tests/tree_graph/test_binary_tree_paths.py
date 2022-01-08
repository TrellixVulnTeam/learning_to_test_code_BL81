from scripts.tree_graph.binary_tree_paths import Solution, Node
from scripts.tree_graph.printRootToLeafPaths import preorder_pythonic

def creatBTree(data, index):
    pNode = None
    if index < len(data):
        if data[index] == None:
            return
        pNode = Node(data[index])
        pNode.left = creatBTree(data, 2 * index + 1) # [1, 3, 7, 15, ...]
        pNode.right = creatBTree(data, 2 * index + 2) # [2, 5, 12, 25, ...]
    return pNode 

def preorder_pythonic(root):
    return [root.key] + preorder_pythonic(root.left) + preorder_pythonic(root.right) if root else []

class Test:
    test_cases = [
        [[1, 2, 3, None, 5], # case
         [1, 2, 5, 3], # preorder
         ["1->2->5","1->3"]], # expected
    
        [[0, 1, 2, 3, 4, None, None, None, None], [0, 1, 3, 4, 2],
        ["0->1->3", "0->1->4", "0->2"]]
    
    ]


    def test_binaryTreePaths(self):
        solution = Solution()
        for case, preorder, expected in self.test_cases:
            root = creatBTree(case, 0)
            assert preorder_pythonic(root) == preorder
            assert solution.binaryTreePaths(root) == expected


    