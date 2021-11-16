from typing import Dict, List

class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

if __name__ == "__main__":
    node0 = Node(0)
    print(node0)