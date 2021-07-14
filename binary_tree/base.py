class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            self.preorder_print(tree)
        elif traversal_type == "inorder":
            self.inorder_print(tree)
        elif traversal_type == "postorder":
            self.postorder_print(tree)

        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    def preorder_print(self, start):
        """Root->Left->Right"""
        if start:
            print(start.value, end = "->")
            self.preorder_print(start.left)
            self.preorder_print(start.right)

    def inorder_print(self, start):
        """Left->Root->Right"""
        if start:
            
            self.inorder_print(start.left)
            print(start.value, end = "->")
            self.inorder_print(start.right)

    def postorder_print(self, start):
        """Left->Right->Root"""
        if start:
            self.postorder_print(start.left)
            self.postorder_print(start.right)
            print(start.value, end = "->")


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
    tree = Tree(1)
    tree.left = Tree(2)
    tree.right = Tree(3)
    tree.left.left = Tree(4)
    tree.left.right = Tree(5)
    tree.left.right.right = Tree(8)
    tree.right.left = Tree(6)
    tree.right.right = Tree(7)
    # tree.print_tree("preorder")
    tree.print_tree("inorder")
    print()
    tree.print_tree("postorder")