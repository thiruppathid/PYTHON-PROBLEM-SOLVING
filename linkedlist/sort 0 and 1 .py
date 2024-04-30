class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class link:
    def __init__(self):
        self.head=None
        self.temp=None
        self.temp2=None
    def create(self,data):
        new=node(data)
        if(self.head==None):
            self.head=new
            self.temp=new
        else:
            self.temp.next=new
            self.temp=new
    def rotate(self,head,x):
        pos=0
        if(self.head==None):
            return
        elif(pos==x):
            return 0
        for _ in range(x):
            temp2=self.head
            self.temp.next=temp2
            #self.temp2.next=None
            self.temp=temp2
            self.head=self.head.next
        self.temp.next=None
        
    def reverse(self, head, k): 
        if head == None: 
          return None
        current = head 
        next = None
        prev = None
        count = 0
        while(current is not None and count < k): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
            count += 1
    def reverse(self,head,k): 
        if self.head is None: 
            return

        current = self.head 
        prev = None
        count = 0

        while current is not None and count < k: 
            next_node = current.next
            current.next = prev 
            prev = current 
            current = next_node
            count += 1

    # Connect the reversed sublist with the rest of the list
        if next_node is not None:
            self.head.next = self.reverse(next_node, k)

    # Update the head of the list
        self.head = prev

    
    def printl(self):
        cur=self.head
        while cur:
            print(cur.data,end=" ")
            cur=cur.next
l=link()
li=list(map(int,input().split()))
for i in li:
    l.create(i)
#l.rotate(l.head,int(input()))
l.reverse(l.head,3)
l.printl()