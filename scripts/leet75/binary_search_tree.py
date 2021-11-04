class BinarySearchTree:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = BinarySearchTree(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = BinarySearchTree(data)
            else:
                self.right.insert(data)
        return self

    def inorder(self):
        return self._inorder(self)

    def _inorder(self, node):
        if node is not None:
            self._inorder(node.left)
            print(node.data)
            self._inorder(node.right)

    def __str__(self):
        return str(self.data)
        
if __name__ == "__main__":
    bst = BinarySearchTree(8)
    bst.insert(10)
    bst.insert(9)


    bst.inorder()

    # nums = [1, 2, 3, 4, 5]
    # for num in nums:
    #     bst.insert(num)

    # 
    # for x in bst.inorder():
    #     print(x)
