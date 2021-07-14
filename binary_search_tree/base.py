class BST:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end = '-')
        inorder(node.right)

def append(root,data):
    if root is None:
        return BST(data)
    if root.data == data:
        return root
    elif root.data < data:
        root.right = append(root.right,data)
    else:
        root.left = append(root.left, data)
    return root

tree = BST(5)
tree = append(tree, 2)
tree = append(tree, 3)
tree = append(tree, 7)
tree = append(tree, 4)

