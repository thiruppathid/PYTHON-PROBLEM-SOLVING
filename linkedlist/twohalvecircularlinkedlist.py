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
    
    def multiply(self,head1,head2):
        cur1=head1
        cur2=head2
        val1=0
        val=0
        while cur1!=None:
            val=(val*10)+cur1.data
            cur1=cur1.next
        
        while cur2!=None:
            val1=(val1*10)+cur2.data
            cur2=cur2.next
        
        return val*val1
l=link()
l1=link()
li=list(map(int,input().split()))
for i in li:
    l.create(i)
li1=list(map(int,input().split()))
for i in li1:
    l1.create(i)
print(l.multiply(l.head,l1.head))
    
    