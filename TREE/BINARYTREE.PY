class node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

class tree:
    def __init__(self):
        self.root=None
        self.temp=None
    def create(self,data):
        if self.root==None:
            root=node(data)
        else:
            temp=root,flag=0;temp1=root
            while True:
                if temp.left is None:
                    temp.left=node(data)
                    break
                elif temp.right is None:
                    temp.right=node(data)
                    break
                elif flag==0:
                    temp=temp1.left
                    flag=1
                else:
                    temp=temp1.right
                    flag=0
                    temp1=temp1.left
                
t=tree()
li=[1,2,3,4,5,6,7,8,9]
for i in li:
    t.create(i)
