class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class link:
    def __init__(self):
        self.head=None
        
    def create(self,x):
        new=node(x)
        if self.head==None:
            self.head=new
            self.temp=new
        else:
            self.temp.next=new
            self.temp=new
    
    def reverse(self,head):
        cur=head
        prev=None
        #next=None
        while cur:
            next=cur.next
            cur.next=prev
            prev=cur
            cur=next
        return prev
    def dis(self):
        cur1=self.head
        while cur1!=None:
            print(cur1.data,end=" ")
            cur1=cur1.next
    def reorder(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        rev=self.reverse(slow.next)
        slow.next=None
        cur=self.head
        while rev:
            h_next=cur.next
            rev_next=rev.next
            cur.next=rev
            rev.next=h_next
            cur=h_next
            rev=rev_next
l=link()
li=list(map(int,input().split()))
for i in li:
    l.create(i)

#l.reverse(l.head)
l.reorder()
l.dis()
# 1 2 3 4 5 