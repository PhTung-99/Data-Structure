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
    tree.node = Node(5)
    tree.node.left = Node(2)
    tree.node.right = Node(3)
    tree.node.left.left = Node(4)
    tree.node.left.right = Node(5)
    tree.node.left.right.right = Node(8)
    tree.node.right.left = Node(6)
    tree.node.right.right = Node(7)
    print(branchSums(tree.node))

