from base import *

class LevelOrder(Tree):
    def levelorder_print(self, start):
        if start is None:
            return 

        queue = []  
        queue.append(start)
        data = []
        while len(queue) > 0:
            data.append(queue[0].value)
            node = queue.pop(0)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print(data)


if __name__ == "__main__":
    tree = LevelOrder(1)
    tree.left = Tree(2)
    tree.right = Tree(3)
    tree.left.left = Tree(4)
    tree.left.right = Tree(5)
    tree.right.left = Tree(6)
    tree.right.right = Tree(7)
    tree.levelorder_print(tree)
