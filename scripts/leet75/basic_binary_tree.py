"""
Binary Tree in Python (programiz)
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    # need global variable if not in arg b/c recursive
    def traverse_inorder(self, output_return=[]):
        if self.left:
            self.left.traverse_inorder()
        print(self.data, end=" ")
        output_return.append(self.data)
        if self.right:
            self.right.traverse_inorder()
        return output_return

    # need global variable if not in arg b/c recursive
    def traverse_preorder(self, output_return=[]):
        print(self.data, end=" ")

    # need global variable if not in arg b/c recursive
    def traverse_postorder(self, output_return=[]):
        pass

    def depth_of_tree(self):
        pass

    def __str__(self):
        return str(self.data)

def sample_tree():
    node0 = Node(0)
    node0.left, node0.right = Node(1), Node(2)
    node0.left.left, node0.left.right = Node(3), Node(4)
    node0.right.left, node0.right.right = Node(5), Node(6)
    return node0
    

if __name__ ==  "__main__":
    sample_tree_root = sample_tree()

    values = [sample_tree_root.data, sample_tree_root.right.data, sample_tree_root.left.data]

    sample_tree_root.traverse_inorder()
    print(sample_tree_root.dicts)