from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Any, Sequence


@dataclass
class DCNode:
    data: int
    left: DCNode | None = None
    right: DCNode | None = None


class Node:
    def __init__(self, key) -> str:
        self.key = key
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return str(self.key)
    
    
def preorder(root):
    return [root.key] + preorder(root.left) + preorder(root.right) if root else []

def inorder(root):
    return inorder(root.left) + [root.key] + inorder(root.right) if root else []

def createBTree(data, index):
    pNode = None

    if index < len(data):
        if data[index] == None:
            return
        
        pNode = Node(data[index])
        pNode.left = createBTree(data, 2 * index + 1)
        pNode.right = createBTree(data, 2 * index + 2)
    
    return pNode
        
def make_dctree():
    return DCNode(1, DCNode(2, DCNode(4), DCNode(5)), DCNode(3, DCNode(5)))



if __name__ == "__main__":
    print(make_dctree())
    
    data = [0, 1 ,2, 3, 4, 5, None]
    root = createBTree(data, 0)
    print(root)
    print(preorder(root))
    print(inorder(root))