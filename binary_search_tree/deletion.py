from base import *
class Deletion(BST):
    def minValueNode(self,node):
        current = node
    
        # loop down to find the leftmost leaf
        while(current.left is not None):
            current = current.left
    
        return current

    def deleteNode(self,root, data):
    
        # Base Case
        if root is None:
            return root
    
        # If the data to be deleted
        # is smaller than the root's
        # data then it lies in  left subtree
        if data < root.data:
            root.left = self.deleteNode(root.left, data)
    
        # If the kye to be delete
        # is greater than the root's data
        # then it lies in right subtree
        elif(data > root.data):
            root.right = self.deleteNode(root.right, data)
    
        # If data is same as root's data, then this is the node
        # to be deleted
        else:
    
            # Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp
    
            elif root.right is None:
                temp = root.left
                root = None
                return temp
    
            # Node with two children:
            # Get the inorder successor
            # (smallest in the right subtree)
            temp = self.minValueNode(root.right)
    
            # Copy the inorder successor's
            # content to this node
            root.data = temp.data
    
            # Delete the inorder successor
            root.right = self.deleteNode(root.right, temp.data)
    
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
tree.deleteNode(tree.root, 24)
tree.print("preorder")

