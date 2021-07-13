#reverse
#swap
#pair swap
#shift

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

    def merge(self, q):
        p_curr = self.head
        q_curr = q.head
        while(p_curr and q_curr):
            p_next = p_curr.next
            q_next = q_curr.next

            q_curr.next = p_next
            p_curr.next = q_curr


            p_curr = p_next
            q_curr = q_next

    def pair_swap(self):
        temp = self.head
        while(temp and temp.next):
            if (temp.data != temp.next.data):
                temp.data , temp.next.data = temp.next.data, temp.data
            temp = temp.next.next

    def merge_sort(self, llist):
        p = self.head 
        q = llist.head
        s = None
    
        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p 
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s 
        while p and q:
            if p.data <= q.data:
                s.next = p 
                s = p 
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q 
        if not q:
            s.next = p 
        self.head = new_head

    def isPalindrome(self):
        fast = slow = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
    
        node = None
        temp = self.head
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        while node:
            if node.data != temp.data:
                return False
            node = node.next
            temp = temp.next    
        return True
             
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
llist2 = LinkedList()

llist1.append(1)
llist1.append(3)
llist1.append(6)
llist1.append(8)
llist1.append(10)
llist1.append(12)

llist2.append(2)
llist2.append(5)
llist2.append(8)
llist2.append(10)
# llist.pair_swap()
# llist1.merge_sort(llist2)
llist3 = LinkedList()
llist1.merge_sort(llist2)
llist1.printList()

# llist.deletePosition(3)
