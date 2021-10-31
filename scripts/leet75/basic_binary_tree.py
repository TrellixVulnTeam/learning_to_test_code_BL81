print("\n")
"""
Binary Tree in Python (programiz)
"""
from typing import List, Dict
class Node:
    def __init__(self, data: int):
        self.data = data
        self.right = None
        self.left = None

    # need global variable if not in arg b/c recursive
    def traverse_inorder(self, output_return=[]) -> List[int]:
        if self.left:
            self.left.traverse_inorder()
        print(self.data, end=" ")
        output_return.append(self.data)
        if self.right:
            self.right.traverse_inorder()
        return output_return

    # need global variable if not in arg b/c recursive
    def traverse_preorder(self, output_return=[]) -> List[int]:
        print(self.data, end=" ")
        output_return.append(self.data)
        if self.left:
            self.left.traverse_preorder()
        if self.right:
            self.right.traverse_preorder()
        return output_return

    # need global variable if not in arg b/c recursive
    def traverse_postorder(self, output_return=[]) -> List[int]:
        print(f"[INFO] need to implement {self.traverse_postorder.__name__}")

    def depth_of_tree(self) -> int:
        print(f"[INFO] need to implement {self.depth_of_tree.__name__}")

    def __str__(self):
        return str(self.data)

def sample_tree():
    node0 = Node(0)
    node0.left, node0.right = Node(1), Node(2)
    node0.left.left, node0.left.right = Node(3), Node(4)
    node0.right.left, node0.right.right = Node(5), Node(6)
    return node0
    

if __name__ ==  "__main__":
    node0 = sample_tree()

    values = [node0.data, node0.right.data, node0.left.data]
    print(values)

    # fxns = {
    #     "inorder" : node0.traverse_inorder, 
    #     "preorder" : node0.traverse_preorder, 
    #     "postorder" : node0.traverse_postorder
    # }
    # for k,v in fxns.items():
    #     fxns[k]()
    #     print("\n")

    # method_list = [func for func in dir(node0) if callable(getattr(node0, func)) and not func.startswith("__")]
    # print(method_list)

    for f in dir(node0):
        if not f.startswith("__") and callable(getattr(node0, f)):
            print(f)
            getattr(node0, f)()
            print("\n")
