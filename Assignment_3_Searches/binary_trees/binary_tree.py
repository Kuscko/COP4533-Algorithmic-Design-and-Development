class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._add(self.root, key)

    # Recursive helper function to add a key to the tree
    def _add(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._add(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._add(node.right, key)
    
    def find(self, key):
        return self._find(self.root, key)

    # Recursive helper function to find a key in the tree
    def _find(self, node, key):
        if node is None:
            return None
        if node.val == key:
            return node.val
        elif key < node.val:
            return self._find(node.left, key)
        else:
            return self._find(node.right, key)