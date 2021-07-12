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

    def sortedMerge(self, a, b):
        result = None
        if a is None:
            return b
        if b is None:
            return a 
        if a.data <= b.data:
            result = a
            result.next = self.sortedMerge(a.next, b)
        else:
            result = b
            result.next = self.sortedMerge(a, b.next)
        return result
        
    def mergeSort(self, h):
        if h is None or h.next is None:
            return h 
        middle = self.getMiddle(h)
        nexttomiddle = middle.next
        middle.next = None
        left = self.mergeSort(h)
        right = self.mergeSort(nexttomiddle)
        sortedlist = self.sortedMerge(left, right)
        return sortedlist

    def getMiddle(self, head):
        if head is None:
            return head
        slow = head
        fast = head
        while (fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
        return slow

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

