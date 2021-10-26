from __future__ import annotations

class Node:
    # A Node has data variable and pointers to Nodes to its left and right
    def __init__(self, data: int) -> None:
        self.data = data
        self.left: Node | None = None
        self.right: Node | None = None


def display(tree: Node | None) -> None:
    if tree:
        display(tree.left)
        print(tree.data)
        display(tree.right)

n0 = Node(0)
display(n0)


class Solution:
    def init_node(self):
        pass

    def display(self):
        pass