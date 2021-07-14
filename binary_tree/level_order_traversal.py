from base import *

class LevelOrder(Tree):
    def _levelorder_print(self, start):
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
    def levelorder_print(self):
        if self.node:
            self._levelorder_print(self.node)
        else:
            print("None")


if __name__ == "__main__":
    tree = LevelOrder()
    tree.node = Node(5)
    tree.node.left = Node(2)
    tree.node.right = Node(3)
    tree.node.left.left = Node(4)
    tree.node.left.right = Node(5)
    tree.node.left.right.right = Node(8)
    tree.node.right.left = Node(6)
    tree.node.right.right = Node(7)
    tree.levelorder_print()
