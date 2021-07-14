from base import *
class Height(Tree):
    def getHeight(self, node):
        if node is None:
            return 0
        left_height = self.getHeight(node.left)
        right_height = self.getHeight(node.right)
        return 1 + max(left_height, right_height)

if __name__ == "__main__":
#               1
#           /       \  
#          2          3  
#         /  \      /   \
#        4    5     6   7 
    tree = Height(1)
    tree.left = Tree(2)
    tree.right = Tree(3)
    tree.left.left = Tree(4)
    tree.left.right = Tree(5)
    tree.right.left = Tree(6)
    tree.right.right = Tree(7)
    print(tree.getHeight(tree))