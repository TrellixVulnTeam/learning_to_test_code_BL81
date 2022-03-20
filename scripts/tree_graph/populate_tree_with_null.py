# This file contains a function which builds a binary treee from a list which may or may not contain null values. This is helpful because on leet code binary tree questions you often get a list

    # lst = [5,4,8,11,None,13,4,7,2,None,None,None,1]
        
# that contains nulls and you need to be able to construct the binary tree from this list. This function will allow you to populate a binary tree from a list containing nulls.
# KZ 1-2-22

class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
 
def createBTree(data, index):
    pNode = None
    if index < len(data):
        if data[index] == None:
            return
        pNode = Node(data[index])
        pNode.left = createBTree(data, 2 * index + 1) # [1, 3, 7, 15, ...]
        pNode.right = createBTree(data, 2 * index + 2) # [2, 5, 12, 25, ...]
    return pNode 

def preorder_pythonic(root):
    return [root.key] + preorder_pythonic(root.left) + preorder_pythonic(root.right) if root else []


if __name__ == "__main__":
    lst = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    lst = [1, 2, 3, None, 5]

    root = createBTree(lst, 0)
    print(preorder_pythonic(root))
    