from linked_list import * 

def addTwo(l1, l2):

    result = Node(0)
    result_tail = result
    carry = 0
            
    while l1 or l2 or carry:            
        val1  = (l1.data if l1 else 0)
        val2  = (l2.data if l2 else 0)
        carry, out = divmod(val1+val2 + carry, 10)    
                
        result_tail.next = Node(out)
        result_tail = result_tail.next                      
        
        l1 = (l1.next if l1 else None)
        l2 = (l2.next if l2 else None)
               
    return result.next

if __name__ == '__main__':
    llist1 = LinkedList()
    llist1.append(3)
    llist1.append(4)
    llist1.append(2)
    llist1.append(7)

    llist2 = LinkedList()
    llist2.append(4)
    llist2.append(6)
    llist2.append(5)

    head = addTwo(llist1.head, llist2.head)
    llist3 = LinkedList()
    llist3.head = head
    llist3.printList()
    