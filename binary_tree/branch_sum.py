from base import *
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
    sums = []
    branchSumsHelper(root, root.value, sums)
    return sums


def branchSumsHelper(root, runningSum, sums):
    if not root.left and not root.right:
        sums.append(runningSum)
        return

    if root.left:
        runningSum += root.left.value
        branchSumsHelper(root.left, runningSum, sums)
        runningSum -= root.left.value

    if root.right:
        runningSum += root.right.value
        branchSumsHelper(root.right, runningSum, sums)
        runningSum -= root.right.value
tree = Tree(1)
tree.left = Tree(2)
tree.right = Tree(3)
tree.left.left = Tree(4)
tree.left.right = Tree(5)
tree.right.left = Tree(6)
tree.right.right = Tree(7)
print(branchSums(tree))

