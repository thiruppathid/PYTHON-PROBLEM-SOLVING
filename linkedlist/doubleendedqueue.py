lis = []
front = 0  # Set front to 0 instead of -1
rear = 0   # Set rear to 0 instead of -1

def bag_rear(val):
    global front, rear, lis
    lis.append(val)
    rear += 1

def remove_front():
    global front, rear, lis
    if front == rear:
        print("Underflow")
    else:
        lis.pop(0)
        front += 1

def insertfront(val):
    global lis
    lis.insert(0,val)

def poplost():
    global lis
    lis.pop(len(lis)-1)

bag_rear(0)
bag_rear(1)
bag_rear(2)
bag_rear(3)
print("Elements in the bag:", lis)
remove_front()
print("After removing front element:", lis)
insertfront(10)
print(lis)
poplost()
print(lis)
