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
        if self.root:
            self._levelorder_print(self.root)
        else:
            print("None")


if __name__ == "__main__":
    tree = LevelOrder()
    tree.root = Node(5)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.left.right.right = Node(8)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    tree.levelorder_print()
