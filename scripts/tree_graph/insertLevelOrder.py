


def insertLevelOrder(array, root, i, n):
    """
    This function constructs a binary tree from given list in level-order fashion
    """
    # base case for recursion
    if i < n:
        temp = Node(array[i])
        root = temp

        # insert left child
        root.left = insertLevelOrder(array, root.left, 2 * i + 1, n)
        # insert right child
        root.right = insertLevelOrder(array, root.right, 2 * i + 2, n)
        
    return root

def inorder_pythonic(root):
    return inorder_pythonic(root.left) + [root.key] + inorder_pythonic(root.right) if root else []

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 6, 6, 6]
    root = None
    root = insertLevelOrder(array, root, 0, len(array))
    inorder = inorder_pythonic(root)
    print(f'inorder: {inorder}')
    assert inorder_pythonic(root) == [6, 4, 6, 2, 5, 1, 6, 3, 6]