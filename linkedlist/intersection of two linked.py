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
            
    def dis(self):
        new=self.head
        while new:
            print(new.data,end="->")
            new=new.next
            
    def inter(self,head1,head2):
        h1=head1
        re=[]
        h2=head2
        while h1:
            temp=head2
            while temp:
                if temp.data==h1.data:
                    print(temp.data,end=" ")
                    re.append(temp.data)
                    break
                temp=temp.next
            h1=h1.next 
        print(*re)
        return re           
l=link()

le=[1,2,3,4,5]
for i in le:
    l.create(i)
l.dis()
print(" ")
l1=link()
le1=[1,2,3,6,7]
for i in le1:
    l1.create(i)
l1.dis()
print(" ")
print("")
l1.inter(l.head,l1.head)