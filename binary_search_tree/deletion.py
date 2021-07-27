from base import *
class Deletion(BST):
    def minValue(self, node):
        curr = node
        while curr.left:
            curr = curr.left    
        return curr 
    
    def _deleteNode(self, root, data):
        if not root:
            return root
        if data < root.data:
            root.left = self._deleteNode(root.left, data)
        elif data > root.data:
            root.right = self._deleteNode(root.right, data)
        else:
            if root.left is None:
                temp = root.right
                return temp
            elif root.right is None:
                temp = root.left
                return temp
            temp = self.minValue(root.right)
            root.data = temp.data
            root.right = self._deleteNode(root.right, temp.data)
        return root
    
    def deleteNode(self, data):
        self.root = self._deleteNode(self.root, data)

    def invert(self):
        self.root = self._invert(self.root)

    def _invert(self, root):
        if root:
            root.left, root.right = self._invert(root.right), self._invert(root.left)
            return root

tree = Deletion()
tree.append(15)
tree.append(8)
tree.append(24)
tree.append(5)
tree.append(19)
tree.append(30)
tree.append(26)
tree.append(25)
tree.append(28)
tree.print("inorder")
tree.deleteNode(24)
# tree.invert()
tree.print("inorder")

