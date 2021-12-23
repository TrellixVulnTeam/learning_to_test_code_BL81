


class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None
        
        
def insert(node, key):
    if node is None:
        print('leaf')
        return Node(key)
    
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    
    # CRITICAL
    print(f'node: {node.key}')
    return node

def inorder_pythonic(root):
    return inorder_pythonic(root.left) + [root.key] + inorder_pythonic(root.right) if root else [] 
        
if __name__ == "__main__":
    root = Node(0)
    insert(root, 1)
    print(inorder_pythonic(root))
    
    print("-------")
    
    insert(root, 2)
    print(inorder_pythonic(root))
