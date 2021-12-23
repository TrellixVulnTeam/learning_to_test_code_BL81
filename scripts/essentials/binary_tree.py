

class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None
        
    def __str__(self):
        return str(self.key)
    

def inorder_pythonic(root):
    return inorder_pythonic(root.left) + [root.key] + inorder_pythonic(root.right) if root else []

def preorder_pythonic(root):
    return [root.key] + preorder_pythonic(root.left) + preorder_pythonic(root.right) if root else []


if __name__ == "__main__":
    root = Node(1)
    
    root.left = Node(2)
    root.right = Node(3)    
    
    root.left.left = Node(4)
    root.left.right = Node(5)
    
    root.left.left.left = Node(6)
    
    root.left.left.left.left = Node(7)
    
    print(inorder_pythonic(root))
    print(preorder_pythonic(root))