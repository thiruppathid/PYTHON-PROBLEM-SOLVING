class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class link:
    def __init__(self):
        self.head=None
        self.temp=None
        self.c=0
    
    def create(self,data):
        new=node(data)
        if self.head is None:
            self.head=new
            self.temp=new
            self.c=1
        else:
            self.temp.next=new
            self.temp=new
            self.c+=1
    
    def rotate(self,k):
        cur=self.head
        prev=node(None)
        if k==0:
            return
        n=self.c
        k=k%n
        for i in range(n-k):
            prev=cur
            cur=cur.next
        prev.next=None
        self.temp.next=self.head
        self.head=cur
    
    def dis(self):
        cur=self.head
        while cur:
            print(cur.data,end=" ")
            cur=cur.next
    def nthnode(self,val):
        n=self.c
        cur=self.head
        for i in range(n-val):
            cur=cur.next
        print(cur.data)
l=link()
li=list(map(int,input().split()))
print(li)
for i in li:
    l.create(i)

#l.rotate(2)
l.nthnode(2)
l.dis()

# 1 2 3 4 5 6
