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
    

def merge_sorted(list1, list2):
    temp = None
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    
    if list1.data <= list2.data:
        temp = list1
        temp.next = merge_sorted(list1.next, list2)
    else:
        temp = list2
        temp.next = merge_sorted(list1, list2.next)
    return temp
    


llist1 = LinkedList()
llist1.append(1)
llist1.append(4)
llist1.append(9)
# llist1.printList()


llist2 = LinkedList()
llist2.append(2)
llist2.append(4)
llist2.append(5)
llist2.append(8)
llist2.append(10)
llist2.append(18)
l = LinkedList()
l.head = merge_sorted(llist1.head, llist2.head)
l.printList()
