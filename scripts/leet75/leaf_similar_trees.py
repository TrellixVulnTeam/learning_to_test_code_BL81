from typing import Optional, Any, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Only need to use this locally
        # tree1 = self.createBTree(root1, 0)
        # tree2 = self.createBTree(root2, 0)
        # return self.get_leafs(tree1) == self.get_leafs(tree2)
        leafs1 = []
        leafs2 = []
        def dfs(root, results):
            if root is None:
                return
            
            if not root.left and not root.right:
                print(f'leaf: {root.val}')
                results.append(root.val)
            
            return dfs(root.left, results) or \
                    dfs(root.right, results)
        dfs(root1, leafs1)
        dfs(root2, leafs2)
        print(leafs1)
        print(leafs2)


    def createBTree(self, data, index):
        pNode = None
        if index < len(data):
            if data[index] == None:
                return
            pNode = TreeNode(data[index])
            pNode.left = self.createBTree(data, 2 * index + 1) # [1, 3, 7, 15, ...]
            pNode.right = self.createBTree(data, 2 * index + 2) # [2, 5, 12, 25, ...]
        return pNode 

    def preorder_pythonic(self, root):
        return [root.val] + self.preorder_pythonic(root.left) + self.preorder_pythonic(root.right) if root else []

if __name__ == '__main__':
    nodes_lst1 = [3,5,1,6,2,9,8,None,None,7,4]
    nodes_lst2 = [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]

    soln = Solution()
    root1 = soln.createBTree(nodes_lst1, 0)
    root2 = soln.createBTree(nodes_lst2, 0)

    print(soln.preorder_pythonic(root1))
    print(soln.preorder_pythonic(root2))

    assert soln.preorder_pythonic(root1) == [3, 5, 6, 2, 7, 4, 1, 9, 8]
    # assert soln.leafSimilar(root1, root2) == True
    print(soln.leafSimilar(root1, root2))