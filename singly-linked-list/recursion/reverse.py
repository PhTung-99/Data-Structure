class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None


    def _printList(self, llist):
        temp = llist
        if temp:
            print(temp.data)
            self._printList(temp.next)

    def printList(self):
        self._printList(self.head)

    # def append(self, data):
    #     temp = self.head
    #     new_node = Node(data)
    #     if not temp:
    #         self.head = new_node
    #         return
    #     while(temp.next):
    #         temp = temp.next
    #     temp.next = new_node        

    def _append(self, llist, data):
        if llist is None:
            llist = Node

        if llist.next is None:
            llist.next = Node(data)
        else:
            self._append(llist.next, data)

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            self._append(self.head, data)

    def _reverse(self, head):
        if not head or not head.next:
            return head
        p = self._reverse(head.next)
        head.next.next = head
        head.next = None
        return p
    def reverse(self):
        self.head = self._reverse(self.head)

# llist1.printList()


llist1 = LinkedList()
llist1.append(2)
llist1.append(4)
llist1.append(5)
llist1.append(8)
llist1.append(10)
llist1.append(18)

llist1.reverse()
llist1.printList()
