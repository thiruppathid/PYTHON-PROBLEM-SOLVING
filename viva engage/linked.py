class node:
    def __init__(self,x):
        self.x=x
        self.next=None
class link:
    def __init__(self):
        self.head=None
        self.temp=self.head
    def create(self,x):
        new=node(x)
        if(self.head==None):
            self.head=new
            head=new
            self.temp=head
        else:
            new=node(x)
            self.temp.next=new
            self.temp=new
    def beg(self,x):
        if(self.head==None):
            l.create(x)
        else:
            new=node(x)
            new.next=self.head
            self.head=new
            l.print()
    def print(self):
        if(self.head==None):
            return
        else:
            cur=self.head
            while(cur):
                print(cur.x,end="->")
                cur=cur.next
    def last(self,x):
        if(self.head==None):
            l.create(x)
        else:
            new=node(x)
            cur=self.head
            while(cur.next):
                cur=cur.next
            cur.next=new
            #l.print()
    def bd1(self):
        if(self.head==None):
            return
        else:
            self.head=self.head.next
        self.print()
    def ld(self):
        if(self.head==None):
            return
        else:
            cur=self.head
            while(cur.next.next!=None):
                cur=cur.next
            cur.next=None
            self.print()
    def re(self):
        pre=None
        cur=self.head
        while(cur is not None):
            next=cur.next
            cur.next=pre
            pre=cur
            cur=next
        self.head=pre
        print(" ")
        self.print()
    def dup(self):
        if(self.head==None):
            return None
        else:
            temp=self.head
            while(temp and temp.next):
                if(temp.x==temp.next.x):
                    temp.next=temp.next.next
                else:
                    temp=temp.next
            self.print()

l=link()
arr=list(map(int,input().split()))
for i in arr:
    l.create(i)
#l.print()
#l.beg(int(input()))
#l.ld()
l.dup()