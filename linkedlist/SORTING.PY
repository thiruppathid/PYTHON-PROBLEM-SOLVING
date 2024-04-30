class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.temp = None

    def create(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            self.temp = new_node
        else:
            self.temp.next = new_node
            self.temp = new_node
        
    def sorting(self):
        if self.head is None or self.head.next is None:
            return
        
        swapped = True
        while swapped:
            swapped = False
            cur = self.head
            while cur.next != self.head:  # Traverse until you reach the head again
                if cur.data > cur.next.data:
                    cur.data, cur.next.data = cur.next.data, cur.data
                    swapped = True
                cur = cur.next
            # Move to the next iteration of outer loop
            # if no swapping is done in the inner loop
            if not swapped:
                break

    def display(self):
        if self.head is None:
            return
        cur = self.head
        while True:
            print(cur.data, end=" ")
            cur = cur.next
            if cur == self.head:
                break

l = LinkedList()
li = list(map(int, input().split()))
for i in li:
    l.create(i)

l.sorting()
l.display()
