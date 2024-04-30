class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.temp = None
        self.st1 = []
        self.st2 = []

    def create(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            self.temp = new_node
        else:
            self.temp.next = new_node
            self.temp = new_node

    def extract(self):
        cur = self.head
        c = 0
        while cur:
            if c == 0:
                self.st1.append(cur.data)
                c = 1
            else:
                self.st2.append(cur.data)
                c = 0
            cur = cur.next

    def newsnode(self):
        c = 0
        dummy = Node(0)
        cur = dummy
        while self.st1 or self.st2:
            if c == 0:
                cur.next = Node(self.st1.pop(0))
                c = 1
            else:
                cur.next = Node(self.st2.pop())
                c = 0
            cur = cur.next
        cur = dummy.next
        while cur:
            print(cur.data, end=" ")
            cur = cur.next

l = LinkedList()
lis = list(map(int, input().split()))
for i in lis:
    l.create(i)

l.extract()
l.newsnode()
