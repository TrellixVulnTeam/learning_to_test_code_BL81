"""
Binary Tree in Python (programiz)
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def traverse_inorder(self):
        pass

    def traverse_preorder(self):
        pass

    def traverse_postorder(self):
        pass

    def depth_of_tree(self):
        pass

    def __str__(self):
        return str(self.data)

def sample_tree():
    node0 = Node(0)
    node0.left, node0.right = Node(1), Node(2)
    node0.left.left, node0.right.right = Node(3), Node(4)
    return node0
    

if __name__ ==  "__main__":
    sample_tree_root = sample_tree()

    values = [sample_tree_root.data, sample_tree_root.right.data, sample_tree_root.left.data]

    print("{}, {}, {}".format(
        values[0], 
        values[1], 
        values[2]
        ))
