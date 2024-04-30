class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class link:
    def __init__(self):
        self.head=None
        self.temp=None
        
    def create(self,data):
        new=node(data)
        if(self.head==None):
            self.head=new
            self.temp=new
        else:
            self.temp.next=new
            self.temp=new
    
    def printl(self):
        if(self.head==None):
            return
        else:
            cur=self.head
            while cur:
                print(cur.data,end=" ")
                cur=cur.next
    
    def delete(self,head,x):
        y=0
        cur=head
        prev=self.head
        if(cur==None or y==x or x==1):
            return
        else:
            cur=head
            while cur and cur.next:
                y+=1
                if(y==x):
                    prev.next=cur.next
                    y=0
                else:
                    prev=cur
                cur=cur.next

l=link()
li=list(map(int,input().split()))
for i in li:
    l.create(i)

l.printl()

print(" ")
a=int(input("enter differnece"))
l.delete(l.head,a)
l.printl()

            