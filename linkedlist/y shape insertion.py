class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def insert(head1,head2):
    while head2:
        temp=head1
        while temp:
            if temp==head2:
                return head2
            temp=temp.next
        head2=head2.next            
                
# Driver Code
if __name__ == '__main__':
    '''
    Create two linked lists
 
    1st 3->6->9->15->30
    2nd 10->15->30
 
    15 is the intersection point 
    '''
 
    newNode = Node(10)
    head1 = newNode
    newNode = Node(3)
    head2 = newNode
    newNode = Node(6)
    head2.next = newNode
    newNode = Node(9)
    head2.next.next = newNode
    newNode = Node(15)
    head1.next = newNode
    head2.next.next.next = newNode
    newNode = Node(30)
    head1.next.next = newNode
    intersectionPoint =insert(head1, head2)
 
    if not intersectionPoint:
        print(" No Intersection Point ")
    else:
        print("Intersection Point:", intersectionPoint.data)
 
# This code is contributed by Tapesh(tapeshdua420)