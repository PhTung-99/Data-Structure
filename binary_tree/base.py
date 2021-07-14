class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.value = data

class Tree:
    def __init__(self):
        self.node = None

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            self.preorder_print(self.node)
        elif traversal_type == "inorder":
            self.inorder_print(self.node)
        elif traversal_type == "postorder":
            self.postorder_print(self.node)

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
    tree = Tree()
    tree.node = Node(5)
    tree.node.left = Node(2)
    tree.node.right = Node(3)
    tree.node.left.left = Node(4)
    tree.node.left.right = Node(5)
    tree.node.left.right.right = Node(8)
    tree.node.right.left = Node(6)
    tree.node.right.right = Node(7)
    # tree.print_tree("preorder")
    tree.print_tree("inorder")
    print()
    tree.print_tree("postorder")