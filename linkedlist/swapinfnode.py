class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class link:
    def __init__(self):
        self.head = None
        
    def create(self, x):
        new = node(x)
        if self.head == None:
            self.head = new
            self.temp = new
        else:
            self.temp.next = new
            self.temp = new
            
    def check(self, head, x, y):
        cur = head
        x_found = 0
        y_found = 0
        while cur:
            if cur.data == x:
                x_found = 1
            elif cur.data == y:
                y_found = 1
            cur = cur.next
        if x_found and y_found:
            self.swap(head, x, y)
        else:
            return False
        
    def swap(self, head, x, y):
        prevX = None
        currX = head
        while currX and currX.data != x:
            prevX = currX
            currX = currX.next
        prevY = None
        currY = head
        while currY and currY.data != y:
            prevY = currY
            currY = currY.next
        
        if not currX or not currY:
            return

        if prevX:
            prevX.next = currY
        else:
            head = currY

        if prevY:
            prevY.next = currX
        else:
            head = currX

        temp = currX.next
        currX.next = currY.next
        currY.next = temp

    def display(self):
        cur = self.head
        while cur.next:
            print(cur.data, end="->")
            cur = cur.next
        print(cur.data)

# Example usage
ll= link()
lis=list(map(int,input().split()))
for i in lis:
    ll.create(i)

print("Original list:")
ll.display()

ll.check(ll.head, 2, 3)
print("After swapping 2 and 3:")
ll.display()
