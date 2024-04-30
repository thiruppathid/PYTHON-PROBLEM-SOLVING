class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class ddl():
    def __init__(self):
        self.front=None
        self.rear=None
        
    def create(self,data):
        new=node(data)
        if(front is None):
            self.front=new
            self.rear=new
            