from main import * 
class Selection_Sort(LinkedList):
    def selection_sort(self):
        temp = self.head
        while(temp):
            minn = temp
            r = temp.next
            while(r):
                if (minn.data > r.data):
                    minn = r
                r = r.next
            x = temp.data
            temp.data = minn.data
            minn.data = x
            temp = temp.next
                
if __name__ == "__main__":
    llist = Selection_Sort()

    llist.append(15)
    llist.append(10)
    llist.append(5)
    llist.append(20)
    llist.append(3)
    llist.append(2)
    llist.append(5)
    llist.append(25)
    llist.append(35)
    llist.append(7)
    llist.selection_sort()

    llist.printList()