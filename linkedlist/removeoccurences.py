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
    def remove(self,head1,val):
        dum=node(0)
        dum.next=head1
        prev=None
        prev,cur=dum,head1
        while cur:
            if(cur.data==val):
                prev.next=cur.next
            else:
                prev=cur
            cur=cur.next
        return dum.next
    def dup(self,head):
        '''
        dum=node(0)
        prev=None
        dum.next=head
        prev,cur=dum,head
        seen=set()
        while cur:
            if (cur.data in seen):
                prev.next=cur.next
            else:
                seen.add(cur.data)
                prev=cur
            cur=cur.next
        return dum.next '''
        dum=node(0)
        prev=None
        dum.next=head
        seen=set()
        prev,cur=dum,head
        while cur:
            if(cur.data in seen):
                prev.next=cur.next
            else:
                seen.add(cur.data)
                prev=cur
            cur=cur.next
        return dum.next
    
    def rotateRight(self, head,k):
        
        if not head:    
            return None
        
        lastElement = head
        length = 1
        # get the length of the list and the last node in the list
        while ( lastElement.next ):
            lastElement = lastElement.next
            length += 1

        # If k is equal to the length of the list then k == 0
        # ElIf k is greater than the length of the list then k = k % length
        k = k % length
            
        # Set the last node to point to head node
        # The list is now a circular linked list with last node pointing to first node
        lastElement.next = head
        
        # Traverse the list to get to the node just before the ( length - k )th node.
        # Example: In 1->2->3->4->5, and k = 2
        #          we need to get to the Node(3)
        tempNode = head
        for _ in range( length - k - 1 ):
            tempNode = tempNode.next
        
        # Get the next node from the tempNode and then set the tempNode.next as None
        # Example: In 1->2->3->4->5, and k = 2
        #          tempNode = Node(3)
        #          answer = Node(3).next => Node(4)
        #          Node(3).next = None ( cut the linked list from here )
        answer = tempNode.next
        tempNode.next = None
        
        return answer

l=link()
lis=list(map(int,input().split()))
for i in lis:
    l.create(i)
res=l.rotateRight(l.head,2)
while res:
    print(res.data,end= " ")
    res=res.next
