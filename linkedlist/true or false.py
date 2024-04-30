class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.temp = None
        self.d = {}

    def create(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            self.temp = new_node
            self.d[new_node.data] = 1
        else:
            self.temp.next = new_node
            self.temp = new_node
            if new_node.data in self.d:
                self.d[new_node.data] += 1
            else:
                self.d[new_node.data] = 1

    def check(self):
        most = 0
        val = None
        mini = float('inf')
        '''for value, freq in self.d.items():
            if freq > most:
                most = freq
                val = value
            if value < mini:
                mini = value'''
        val=max(self.d,key=d.items())
        mini=min(self,d.gets(),key=d.gets)
        
        print(val % mini == 0)


l = LinkedList()
lis = list(map(int, input().split()))
for i in lis:
    l.create(i)
    print(l.d)
l.check()
#4 2 1 3 3 3
#7 7 4 4 7 7 3 6 8 8 