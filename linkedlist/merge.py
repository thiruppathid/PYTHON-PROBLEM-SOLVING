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
            
    def merge1(self,headA,headB):
        dummy=node(0)
        tail=dummy
        while True:
            if headA is None:
                tail.next=headB
                break
            if headB is None:
                tail.next=headA
                break
            if(headA.data<=headB.data):
                tail.next=headA
                headA=headA.next
            else:
                tail.next=headB
                headB=headB.next
        
            tail=tail.next
        return dummy.next

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
 
# Create 2 lists
listA = link()
listB = link()
 
# Add elements to the list in sorted order
listA.create(5)
listA.create(10)
listA.create(15)
listB.create(2)
listB.create(3)
listB.create(20)
listA.head = listA.merge1(listA.head,listB.head)

listA.printList()
