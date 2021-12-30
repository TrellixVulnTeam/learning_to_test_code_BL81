


def insertLevelOrder(array, root, i, n):
    """
    This function constructs a binary tree from given list in level-order fashion
    """
    pass

def inorder_pythonic(root):
    return inorder_pythonic(root.left) + [root.key] + inorder_pythonic(root.right) if root else []

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
