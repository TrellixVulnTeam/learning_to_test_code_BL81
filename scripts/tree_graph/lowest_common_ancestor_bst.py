

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

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        pass

    def bfs(self, root, p, q):
        output = []

        if root is None:
            return root
        
        process_queue = [root]
        while process_queue:
            node = process_queue.pop(0)
            output.append(node.key)

            if (node.left.key == p and node.right.key == q) \
                or (node.left.key == q and node.right.key == p):
                return node.key



if __name__ == "__main__":
    root = [6,2,8,0,4,7,9,None,None,3,5]
    p, q = 2, 8
    
    # root = [6,2,8,0,4,7,9,None,None,3,5]
    # p, q = 2, 4


    root = createBTree(root, 0)
    print(preorder_pythonic(root))

    solution = Solution()
    print(solution.bfs(root, p, q))
    # assert solution.lowestCommonAncestor(root, p, q) == 6

    def test():
        nums = [1, 2, 3, 4, 5]
        l, r = 0, len(nums) -1
        while l <= r:
            print(nums[l], nums[r])
            l += 1
            r -= 1
    
    
    test()