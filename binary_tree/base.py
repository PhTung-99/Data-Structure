from math import inf
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class Tree:
    def __init__(self):
        self.root = None

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            self.preorder_print(self.root)
        elif traversal_type == "inorder":
            self.inorder_print(self.root)
        elif traversal_type == "postorder":
            self.postorder_print(self.root)

        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    def preorder_print(self, start):
        """Root->Left->Right"""
        if start:
            print(start.data, end = "->")
            self.preorder_print(start.left)
            self.preorder_print(start.right)

    def inorder_print(self, start):
        """Left->Root->Right"""
        if start:
            
            self.inorder_print(start.left)
            print(start.data, end = "->")
            self.inorder_print(start.right)

    def postorder_print(self, start):
        """Left->Right->Root"""
        if start:
            self.postorder_print(start.left)
            self.postorder_print(start.right)
            print(start.data, end = "->")
            
    def _isBST(self, node, max, min):
        if not node:
            return True
        if node.data <= min:
            return False
        if node.data >= max:
            return False
        return self._isBST(node.left, node.data, min) and self._isBST(node.right, max, node.data)


    def isBST(self):
        return self._isBST(self.root, float("inf"), float("-inf"))


# 1-2-4-5-3-6-7
# 4-2-5-1-6-3-7
# 4-2-5-6-3-7-1
#               1
#           /       \  
#          2          3  
#         /  \      /   \
#        4    5     6   7 

# Set up tree:
if __name__ == "__main__":
    tree = Tree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    # tree.print_tree("preorder")
    tree.print_tree("inorder")
    print(tree.isBST())
    tree.print_tree("postorder")