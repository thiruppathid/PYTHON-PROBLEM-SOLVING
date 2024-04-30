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
    def begining(self,x):
        new=node(x)
        if self.head==None:
            self.head=new
            #self.temp=new
        else:
            new.next=self.head
            self.head=new
    def las(self,x):
        new=node(x)
        if(self.head==None):
            self.head=new
            return
        #cur=self.head
        self.temp.next=new
        self.temp=new
    def print(self):
        cur=self.head
        while(cur.next!=None):
            print(cur.data,end="->")
            cur=cur.next
        print(cur.data)
    def update(self,val,idx):
        cur=self.head
        pos=0
        if(pos==idx):
            cur.data=val
        else:
            while(cur!=None and pos!=idx):
                pos+=1
                cur=cur.next
            if(cur!=None):
                cur.data=val
            else:
                print("not index")
    def begdel(self):
        if(self.head==None):
            return
        self.head=self.head.next
    def lasdel(self):
        if(self.head==None):
            return 
        cur=head.next
        while(cur.next.next):
            cur=cur.next
        cur.next=None
    def particularindexdelete(self,idx):
        cur=self.head
        pos=0
        if(pos==idx):
            self.begdel()
        else:
            while(cur!=None and pos+1!=idx):
                pos+=1
                cur=cur.next
            if(cur.next!=None):
                cur.next=cur.next.next
            else:
                print("Not index")
    def count(self):
        c=0
        if(self.head):
            cur=self.head
            while(cur):
                c+=1
                cur=cur.next
            return c
    def search(self,val):
        pos=0
        cur=self.head
        if(self.head):
            cur=self.head
            while(cur):
                if(cur.data==val):
                    print("Founded",pos)
                    return
                else:
                    cur=cur.next
                    pos+=1
        else:
            return 0
                
l=link()
lis=list(map(int,input().split()))
for i in lis:
    l.create(i)
l.print()
l.las(int(input()))
l.print()


    
