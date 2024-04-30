class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class link:
    def __init__(self):
        self.front=None
        self.rear=None
    def create(self,data):
        new=node(data)
        if(self.front==None):
            self.front=new
            self.rear=new
        else:
            self.rear.next=new
            self.rear=new
    def enq(self,data):
        new=node(data)
        if self.front is None:
            self.create(data)
        else:
            self.rear.next=new
            self.rear=new
    def enqfront(self,data):
        if(self.front is None):
            self.create(data)
        else:
            new=node(data)
            new.next=self.front
            self.front=new
    def deq(self):
        if self.front is None:
            print("empty")
            return
        elif self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.front=self.front.next
            if self.front is None:
                self.rear=None
                self.rear=None
    def ltdeq(self):
        if self.front is None:
            print("empty")
            return
        else:
            temp=self.front
            while temp.next.next:
                temp=temp.next
            temp.next=None
obj=link()
li=list(map(int,input().split()))
for i in li:
    obj.create(i)
print(obj.rear.data)
obj.deq()
print(obj.front.data)
obj.enqfront(15)
obj.ltdeq()
temp=obj.front
while temp:
    print(temp.data,end=" ")
    temp=temp.next
