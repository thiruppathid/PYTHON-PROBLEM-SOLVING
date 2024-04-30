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
            new=self.temp
        else:
            new.next=self.head
            self.head=new
    def display(self):
        new=self.head
        while new.next!=None:
            print(new.data,end="->")
            new=new.next
        print(new.data)
    def pop(self):
        if(self.head==None):
            return
        else:
            self.head=self.head.next

obj=link()
li=list(map(int,input().split()))
for i in li:
    obj.create(i)
obj.display()
obj.pop()
obj.display()
print(obj.head.data)