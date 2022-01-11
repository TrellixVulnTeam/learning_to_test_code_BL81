



class Node:
    def __init__(self, key: int) -> None:
        self.key = key
        self.left = None
        self.right = None
    
    def __str__(self) -> str:
        return str(self.key)

def preorder(root: Node):
    return [root.key] + preorder(root.left) + preorder(root.right) if root else []

def inorder(root: Node):
    return inorder(root.left) + [root.key] + inorder(root.right) if root else []

def preorder_verbose(root: Node):
    if root:
        print(root.key)
        preorder_verbose(root.left)
        preorder_verbose(root.right)

def insert(node: Node, key: int) -> None:
    if node is None:
        return Node(key)
    
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    
    # important for upward recursion steps to preserve tree structure as we move back up the tree during recursion
    return node

def minValueNode(node: Node) -> Node:
    # return in-order successor
    current = None

    # find the leftmost leaf
    while current.left is not None:
        current = current.left
    
    return current


def deleteNode(root: Node, key: int) -> None:
    # return if the tree is empty
    if root is None:
        return root

    # find node to be deleted
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif key > root.key:
        root.right = deleteNode(root.right, key)
    else:
        # if node has one or no children
        if root.left is None:
            temp = root.right
            root = None
            return temp
        
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        
        else:
            # if node has two children, replace with inorder successor with the node to be deleted
            temp = minValueNode(root.right)
            
            root.key = temp.key

            # delete the inorder successor
            root.right = deleteNode(root.right, temp)
            
    return root

def tree_build():
    root = None
    root = insert(root, 8)
    root = insert(root, 3)
    root = insert(root, 1)
    root = insert(root, 6)
    root = insert(root, 10)
    root = insert(root, 4)
    return root



if __name__ == "__main__":
    root = Node(0)
    root = insert(root, 1)
    root = insert(root, 2)
    
    print(preorder(root))
    # assert 
    
    root = deleteNode(root, 2)
    print(preorder(root))
    
    # print(root.key)
    # print(root.left, root.right)