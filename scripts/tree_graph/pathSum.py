from typing import List, Optional


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: Optional[Node], targetSum: int) -> bool:
        def dfs(node, curSum):
            if node is None:
                return False
            
            curSum += node.key
            if not node.left and not node.right:
                return curSum == targetSum
            
            return dfs(node.left, curSum) or \
                    dfs(node.right, curSum)

        return dfs(root, 0)


def inorder_pythonic(root):
    return inorder_pythonic(root.left) + [root.key] + inorder_pythonic(root.right) if root else []

def preorder_pythonic(root):
    return [root.key] + preorder_pythonic(root.left) + preorder_pythonic(root.right) if root else []

if __name__ == "__main__":
    root = Node(5)
    root.left = Node(4)
    root.right = Node(8)
    root.left.left = Node(11)
    root.left.left.left = Node(7)
    root.left.left.right = Node(2)
    root.right.left = Node(13)
    root.right.right = Node(4)
    root.right.right.right = Node(1)
    print(inorder_pythonic(root))
    print(preorder_pythonic(root))
    
    solution = Solution()
    print(solution.hasPathSum(root, 27))
