# basic binary tree
from typing import List, Dict

class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

def create_tree() -> None:
    node0 = Node(0)
    node0.left = Node(1)
    node0.right = Node(2)
    return node0

def inorder(root: Node) -> None:
    pass

def inorder_pythonic(root: Node) -> None:
    return inorder_pythonic(root.left) + [root.data] + inorder_pythonic(root.right) if root else []

if __name__ == "__main__":
    node0 = create_tree()
    print(node0.left.data)