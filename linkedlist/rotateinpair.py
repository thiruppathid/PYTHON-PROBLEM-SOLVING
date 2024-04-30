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
    
    def swap(self,x):
        if(x==0 or x==1):
            return
        cur=self.head
        prev=None
        c=1
        while cur and c!=x:
            prev=cur
            cur=cur.next
            c+=1
        temp=self.head
        prev.next=temp
        temp.next=cur
        cur=self.head
        cur.next=self.head.next
        