#print linkedlist
#push linkedlist
#append linkedlist
#deleteNode
#deletePosition
#get
#len(LinkedList)

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

    def deleteNode(self, key):
        temp = self.head
        if (temp is not None):
            if(temp.data == key):
                self.head = temp.next
                temp = None
                return
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return 
        prev.next = temp.next
        temp = None

    def deletePosition(self, position):
        if self.head == None:
            return
        temp = self.head

        if position == 0:
            self.head = temp.next
            temp = None
            return 
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break

        if temp is None:
            return
        
        if temp.next is None:
            return

        next = temp.next.next
        temp.next = None

        temp.next = next

    def get(self, data):
        if self is None or data is None:
            return
        index = 0
        temp = self.head
        while(temp):
            if (temp.data == data):
                return index
            else:
                temp = temp.next
                index = index + 1

    def reverse(self):
        current = self.head
        prev = None
        while(current):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def __len__(self):
        current = self.head
        count = 0
        while (current):
            count = count + 1
            current = current.next
        return count

    
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

llist = LinkedList()
# Create a list 10->20->30->40->50->60
for i in range(60, 0, -10):
    llist.append(i)

# llist.deleteNode(5)

llist.printList()
print("------")
llist.reverse()
llist.printList()
print("Length: " + str(len(llist)))
# llist.deletePosition(3)
# print(llist.get(12))

