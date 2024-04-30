class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class link:
    def __init__(self):
        self.head=None
        self.st=[]
    def create(self,data):
        new=node(data)
        if(self.head==None):
            self.head=new
            self.temp=new
        else:
            self.temp.next=new
            self.temp=new
    def stack(self):
        cur=self.head
        while(cur):
            self.st.append(cur.data)
            cur=cur.next
    def polindrome(self,mid):
        #last=self.st.pop()
        pos=0
        cur=self.head
        while(cur):
            last=self.st.pop()
            if(cur.data==last and pos!=mid):
                cur=cur.next
                pos+=1
            elif(pos==mid):
                print("yes")
                return
            else:
                print("NO")
                return
                
l=link()
var=input()
for i in range(len(var)):
    l.create(var[i])
l.stack()
l.polindrome(2)
            
            
        