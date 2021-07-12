class Node:
    def __init__(self, head): 
        self.data = head
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    # insert at beginning 
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:   
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node



    
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

if __name__ == "__main__":
    llist = LinkedList()

    llist.append(15)
    llist.append(10)
    llist.append(5)
    llist.append(20)
    llist.append(3)
    llist.append(2)
    llist.append(5)
    llist.append(25)
    llist.head = llist.mergeSort(llist.head)
    llist.printList()

