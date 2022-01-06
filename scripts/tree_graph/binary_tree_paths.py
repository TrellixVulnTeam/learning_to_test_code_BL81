"""
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

# Definition for a binary tree node.
# class Node:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""


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
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.key)

class Solution:
    def binaryTreePaths(self, root):
        res = []
        stk = [(root, str(root.key))]
        
        while stk:
            curr, path = stk.pop()
            
            if curr:
                if curr != root:
                    path += "->" + str(curr.key)
                
                if curr.right:
                    stk.append((curr.right, path))
                
                if curr.left:
                    stk.append((curr.left, path))
                    
                if not curr.left and not curr.right:
                    res.append(path)
                    
        return res
    
    
if __name__ == "__main__":
    data = [1,2,3,None,5]
    root = None
    root = creatBTree(data, 0)
    print(preorder_pythonic(root))
    
    solution = Solution()
    print(solution.binaryTreePaths(root))