from base import *

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
if __name__ == "__main__":
    tree = Tree()
    tree.root = Node(5)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.left.right.right = Node(8)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    print(branchSums(tree.root))

