#reverse
#swap
#pair swap
#shift

from timeit import default_timer as timer


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

    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current 
            current = next
        self.head = prev

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def swap_node(self, x, y):
        if x == y:
            return
        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != x:
            prev_1 = curr_1
            curr_1 = curr_1.next
        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != y:
            prev_2 = curr_2
            curr_2 = curr_2.next
        if not curr_1 and not curr_2:
            return
        
        if prev_1:
            prev_1.next= curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1
        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    def shift(self, k):
        if (not self.head):
            return 
    
        # len is used to store length of the linked list
        # tmp will point to the last node after this loop
        tmp = self.head
        len = 1
    
        while (tmp.next != None):
            tmp = tmp.next
            len += 1
    
        # If k is greater than the size
        # of the linked list
        if (k > len):
            k = k % len
    
        # Subtract from length to convert
        # it into left rotation
        k = len - k
    
        # If no rotation needed then
        # return the head node
        if (k == 0 or k == len):
            return 
    
        # current will either point to
        # kth or None after this loop
        current = self.head
        cnt = 1
    
        while (cnt < k and current != None):
            current = current.next
            cnt += 1
        
        next = LinkedList()
        temp = self.head
        for i in range(cnt):
            if (temp.next is not None):
                next.append(temp.data)
                temp = temp.next

        

    
        # If current is None then k is equal to the
        # count of nodes in the list
        # Don't change the list in this case
        if current is None:
            return
        temp_cur = current
        while(temp_cur.next):
            temp_cur = temp_cur.next
        temp_cur.next = next.head
        self.head = current.next
    
        # current points to the kth node
    
        # Return the updated head pointer
        
    def rightRotate(self, k):
 
    # If the linked list is empty
        if (not self.head):
            return self.head
    
        # len is used to store length of the linked list
        # tmp will point to the last node after this loop
        tmp = self.head
        len = 1
    
        while (tmp.next != None):
            tmp = tmp.next
            len += 1
    
        # If k is greater than the size
        # of the linked list
        if (k > len):
            k = k % len
    
        # Subtract from length to convert
        # it into left rotation
        k = len - k
    
        # If no rotation needed then
        # return the head node
        if (k == 0 or k == len):
            return
    
        # current will either point to
        # kth or None after this loop
        current = self.head
        cnt = 1
    
        while (cnt < k and current != None):
            current = current.next
            cnt += 1
    
        # If current is None then k is equal to the
        # count of nodes in the list
        # Don't change the list in this case
        if (current == None):
            return
    
        # current points to the kth node
    
        # Change next of last node to previous head
        tmp.next = self.head
        cnt = 1
        self.head = current.next
        temp = self.head
        while(cnt<len and temp):
            temp = temp.next
            cnt += 1
        temp.next = None
    
        

    def pair_swap(self):
        temp = self.head
        while(temp and temp.next):
            if (temp.data != temp.next.data):
                temp.data , temp.next.data = temp.next.data, temp.data
            temp = temp.next.next
llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.append("E")
llist.append("F")
llist.append("G")
llist.append("H")
llist.append("I")
llist.append("J")
llist.append("K")
llist.append("L")

llist1 = LinkedList()
llist1.append("A")
llist1.append("B")
llist1.append("C")
llist1.append("D")
llist1.append("E")
llist1.append("F")
llist1.append("G")
# llist.pair_swap()
start = timer()
llist.shift(10)
end = timer()
print(end - start)

llist.printList()


print('-------')
start = timer()
llist1.rightRotate(3)
end = timer()
print(end - start)
llist1.printList()

# llist.deletePosition(3)

