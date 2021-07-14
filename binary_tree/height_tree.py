from base import *
class Height(Tree):
    def _getHeight(self, node):
        if node is None:
            return 0
        left_height = self._getHeight(node.left)
        right_height = self._getHeight(node.right)
        return 1 + max(left_height, right_height)

    def getHeight(self):
        if self.node:
            return self._getHeight(self.node)
        else:
            print("0 - Tree is None")

#               1
#           /       \  
#          2          3  
#         /  \      /   \
#        4    5     6   7 
#              \
#               8
if __name__ == "__main__":
    tree = Height()
    tree.node = Node(5)
    tree.node.left = Node(2)
    tree.node.right = Node(3)
    tree.node.left.left = Node(4)
    tree.node.left.right = Node(5)
    tree.node.left.right.right = Node(8)
    tree.node.right.left = Node(6)
    tree.node.right.right = Node(7)
    print(tree.getHeight())