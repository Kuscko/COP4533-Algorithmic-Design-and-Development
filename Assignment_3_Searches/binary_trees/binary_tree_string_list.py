from binary_tree import BinaryTree

class BinaryTreeStringList:
    def __init__(self):
        self.tree = BinaryTree()

    def add(self, string):
        self.tree.add(string)

    def find(self, string):
        return self.tree.find(string)