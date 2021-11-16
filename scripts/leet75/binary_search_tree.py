from time import strftime, strptime


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
        if node:
            self._inorder(node.left)
            print(node.data)
            self._inorder(node.right)

    def __str__(self):
        return str(self.data)

if __name__ == "__main__":
    import time
    from datetime import datetime

    bst = BinarySearchTree(8)
    bst.insert(10)
    bst.insert(9)
    bst.inorder()

    start = time.perf_counter()
    nums = [i for i in range(1001)]
    for num in nums:
        bst.insert(num)
    duration = time.perf_counter() - start
    print(f"duration: {duration:.3f} seconds")

    # print(f"duration: {(start - time.perf_counter()) * 1000:.1f}ms")

    # for x in bst.inorder():
    #     print(x)
    bday = "2021-06-25 15:25:56"
    print(type(datetime.strptime(bday, "%Y-%m-%d %H:%M:%S")))
    bday_obj = datetime.strptime(bday, "%Y-%m-%d %H:%M:%S")
    print(f"hour: {bday_obj.hour}")

    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    nrows = len(matrix)
    ncols = len(matrix[0])

    maze = [[num for num in row] for row in matrix]
    print(maze)
