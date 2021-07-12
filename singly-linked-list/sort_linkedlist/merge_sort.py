from main import *
class Merge_Sort(LinkedList):
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
    llist = Merge_Sort()

    llist.append(15)
    llist.append(21)
    llist.append(24)
    llist.append(17)
    llist.append(23)
    llist.append(10)
    llist.append(5)
    llist.head = llist.mergeSort(llist.head)
    llist.printList()
    