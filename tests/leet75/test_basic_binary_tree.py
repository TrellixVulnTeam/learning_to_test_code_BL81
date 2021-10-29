from scripts.leet75.basic_binary_tree import Node, sample_tree

class Test:
    test_cases = [
        [Node(0), 0],
        [Node(1), 1]
    ]
    testable_functions = ["traverse_inorder", "traverse_preorder", "traverse_postorder", "depth_of_tree"]

    def test_node_str(self):
        node = Node(0)
        assert type(node.__str__()) == str
        assert node.__str__() == str(node.data)

    def test_sample_tree(self):
        # returns root node of built-tree
        sample_tree_root = sample_tree()
        assert [0, 2, 1] == [sample_tree_root.data, sample_tree_root.right.data, sample_tree_root.left.data]

    def test_traversal_inorder(self):
        pass
