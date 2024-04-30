class node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class double():
    def __init__(self):
        self.head=None
    
    def create(self,data):
        new=node(data)
        if(self.head==None):
            self.head=new
            self.temp=new
        else:
            self.temp.next=new
            new.prev=self.temp
            self.temp=new
    def beginsert(self,data):
        if(self.head==None):
            self.create(data)
        else:
            new=node(data)
            new.next=self.head
            self.head.prev=new
            self.head=new
    def lastinsert(self,data):
        if(self.head==None):
            self.beginsert(data)
        else:
            new=node(data)
            self.temp.next=new
            new.prev=self.temp
            self.temp=new
    def insertmiddle(self,mid,data):
        pos=0
        if(mid==0):
            self.beginsert(data)
        else:
            cur=self.head
            while(cur and pos!=mid-1):
                cur=cur.next
                pos+=1
            if(cur!=None):
                new=node(data)
                new.next=cur.next
                cur.next.prev=new
            cur.next=new
            new.prev=cur
    def deletebegin(self):
        if(self.head==None):
            return
        else:
            self.head=self.head.next
            self.head.next.prev=self.head
    def lastdelete(self):
        if self.head==None:
            return
        else:
            self.temp.prev.next=None
        '''else:
            cur=self.head
            while(cur.next.next):
                cur=cur.next
            cur.next.prev=None
            cur.next=None'''
    def deletemiddle(self,idx):
        if(self.head==None):
            return
        else:
            pos=0
            if(pos==idx):
                self.deletebegin()
            else:
                cur=self.head
                while(cur and pos!=idx):
                    cur=cur.next
                    pos+=1
                if(cur):
                    cur.prev.next=cur.next
                    if cur.next:
                        cur.next.prev=cur.prev
    def count(self):
        c=0
        cur=self.head
        while(cur):
            c+=1
            cur=cur.next
        mid=c//2
        self.insertmiddle(mid,int(input()))
        
    def print(self):
        cur=self.head
        while(cur.next!=None):
            print(cur.data,end="->")
            cur=cur.next
        print(cur.data)
            
l=double()
lis=list(map(int,input().split()))
for i in lis:
    l.create(i)
l.print()
l.deletemiddle(int(input()))
l.print()