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
        if start is None:
            return
    
        nodeStack = []
        nodeStack.append(start)

        while(len(nodeStack) > 0):
            
            node = nodeStack.pop()
            print (node.value, end=" ")
            
            if node.right is not None:
                nodeStack.append(node.right)
            if node.left is not None:
                nodeStack.append(node.left)

    def inorder_print(self, start):
        """Left->Root->Right"""
        current = start
        stack = [] # initialize stack
        
        while True:
            if current is not None:
                stack.append(current)
                current = current.left

            elif(stack):
                current = stack.pop()
                print(current.value, end=" ")
                current = current.right
            else:
                break

    def postorder_print(self, start):
        """Left->Right->Root"""
        s = []

        cur = start
        is_done = False

        traversal = []
        while not is_done:
             
            if cur is not None:
                s.append(cur)
                cur = cur.left
            else:
                if len(s) > 0:
                    cur = s.pop()
                    traversal.append(cur.value)
                    cur = cur.right
                else:
                    is_done = True
        print(traversal)


# 1-2-4-5-3-6-7 preorder
# 4-2-5-1-6-3-7 inorder
# 4-2-5-6-3-7-1 postorder
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