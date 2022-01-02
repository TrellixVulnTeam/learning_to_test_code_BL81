# This file contains three different ways to find the root to leaf paths and return them in a Binary Tree.
# 1. Recursive 2. Pythonic List Comp. 3. Iterative
# KZ 1-2-22


class Node:
    """
    Class to store binary tree node.
    """
    def __init__(self, key: int) -> None:
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key)
    
def preorder_pythonic(node):
    """
    Pythonic recursive pre-order traversal.
    """
    return [node.key] + preorder_pythonic(node.left) + preorder_pythonic(node.right) if node else []

    
def binaryTreeRootToLeafPythonic(root):
    if root is None: 
        return []
    if root.left is None and root.right is None:
        return [str(root.key)]
    # if left/right is None we'll get empty list anyway
    return [str(root.key) + '->'+ l for l in 
             binaryTreeRootToLeafPythonic(root.right) + binaryTreeRootToLeafPythonic(root.left)]

def binaryTreeRootToLeafRecursive(root):
    if root is None: 
        return []
    if root.left is None and root.right is None:
        return [str(root.key)]

    # subtree is always a list, though it might be empty 
    left_subtree = binaryTreeRootToLeafRecursive(root.left)  
    right_subtree = binaryTreeRootToLeafRecursive(root.right)
    full_subtree = left_subtree + right_subtree  # the last part of comprehension

    list1 = []
    for leaf in full_subtree:  # middle part of the comprehension
        list1.append(str(root.key) + '->'+ leaf)  # the left part 

    return list1

def binaryTreeRootToLeafIterative(root):
    res = []
    stk = [(root, str(root.key))]
    
    while stk:
        curr, path = stk.pop()
        if curr:
            if curr != root:   #since a path won't start with a '->', and we've already set the start of the path as str(root.val)
                path += '->' + str(curr.key)
            if curr.right:
                stk.append((curr.right, path))
            if curr.left:
                stk.append((curr.left, path))
            if not curr.right and not curr.left:
                res.append(path)
    return res

if __name__ == "__main__":
    root = Node(0)
    assert root.key == 0
    assert root.left == root.right == None
    root.left = Node(1)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    
    pythonic = binaryTreeRootToLeafPythonic(root)
    pythonic.reverse()
    print(f'pythonic: {pythonic}')
    
    recursive = binaryTreeRootToLeafRecursive(root)
    print(f'recursive: {recursive}')
    
    iterative = binaryTreeRootToLeafIterative(root)
    print(f'iterative: {iterative}')
    
    assert pythonic == recursive == iterative