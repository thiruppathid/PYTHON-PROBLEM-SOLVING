size = 5
lis = [None] * size

def insert(val):
    global front, rear, lis, size
    if (front == rear == -1):
        front = 0
        rear = 0
        lis[rear] = val
    elif (front == (rear + 1) % size):
        print("Overflow")
    else:
        rear = (rear + 1) % size
        lis[rear] = val
    
def delete():
    global front, rear, lis, size
    if front == -1 and rear == -1:
        print("Underflow")
    elif front == rear:
        front = -1
        rear = -1
    else:
        front = (front + 1) % size

def display():
    global front, rear, lis, size
    if front == -1:
        print("Underflow")
    else:
        i = front
        while i != rear:
            print(lis[i], end=" ")
            i = (i + 1) % size
        print(lis[rear])

front = -1
rear = -1

insert(1)
insert(2)
insert(3)
insert(4)
insert(5)
delete()
delete()
display()
