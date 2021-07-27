from typing import BinaryIO
from base import *
class Invert(BST):

    def _invert(self, node):
        if node:
            node.left, node.right = self._invert(node.right), self._invert(node.left)
            return node
    
    def invert(self):
        self.root = self._invert(self.root)

if __name__ == "__main__":
    tree = Invert()
    tree.append(10)
    tree.append(5)
    tree.append(3)
    tree.append(6)
    tree.append(12)
    tree.append(11)
    tree.append(13)
    tree.print("inorder")
    tree._invert(tree.root)
    tree.print("inorder")
    


