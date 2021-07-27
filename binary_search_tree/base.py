class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BST:
    def __init__(self):
        self.root = None

    def _inorder(self, node, traversal):
        if node:
            self._inorder(node.left, traversal)
            traversal.append(node.data)
            self._inorder(node.right, traversal)
        if traversal:
            return traversal

    def _preorder(self, node, traversal):
        if node:
            traversal.append(node.data)
            self._preorder(node.left, traversal)
            self._preorder(node.right, traversal)
        if traversal:
            return traversal

    def _postorder(self, node, traversal):
        if node:
            self._postorder(node.left, traversal)
            self._postorder(node.right, traversal)
            traversal.append(node.data)
        if traversal:
            return traversal

    def print(self, type) -> str:
        traversal = []
        if type =='inorder':
            print( self._inorder(self.root, traversal))
        elif type == 'preorder':
            print(self._preorder(self.root, traversal))
        elif type == 'postorder':
            print(self._postorder(self.root, traversal))
        else:
            return 'not support ' + type

    def _append(self, node, data):
        if node.data < data:
            if node.right:
                self._append(node.right,data)
            else:
                node.right = Node(data)
        elif node.data == data:
            return 
        else:
            if node.left:
                self._append(node.left, data)
            else:
                node.left = Node(data)
    
    def append(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._append(self.root, data)

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

    def _isFullTree(self, node):
        if node is None:
            return True
        if not node.left and not node.right:
            return True
        if node.left and node.right:
            return self._isFullTree(node.left) and self._isFullTree(node.right)
        else:
            return False

    def isFullTree(self):
        return self._isFullTree(self.root)

    def _getHeight(self, node):
        if node is None:
            return 0
        return 1 + max(self._getHeight(node.left), self._getHeight(node.right))

    def getHeight(self):
        return self._getHeight(self.root)

    def _isPerfectTree(self, node, height, level = 1):
        if node is None:
            return True
        if node.left is None and node.right is None and level <= height:
            return True
        if node.left and node.right:
            return self._isPerfectTree(node.left, height, level + 1) and self._isPerfectTree(node.right, height, level + 1)
        else:
            return False

    def isPerfectTree(self):
        height = self.getHeight()
        return self._isPerfectTree(self.root, height)

if __name__ == "__main__":
    tree = BST()
    tree.append(5)
    tree.append(2)
    tree.append(7)
    tree.append(1)
    tree.append(3)
    tree.append(6)
    # tree.append(9)
    # tree.append(12)
    # tree.append(10)
    # tree.append(11)
    # tree.append(8)
    tree.print('postorder')
    # print(tree.isFullTree())
    print(tree.isPerfectTree())

