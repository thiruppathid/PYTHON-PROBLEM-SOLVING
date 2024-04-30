from collections import defaultdict

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class tree:
    def __init__(self):
        self.root = None
        self.cur = node(None)
        self.c = 0
    
    def create(self, data):
        if self.cur.left is None:
            #self.cur = node(data)
            self.cur.left = node(data)
        elif self.cur.right is None:
            self.cur.right = node(data)
        else:
            self.cur.data = self.cur.left.data + self.cur.right.data
            if data <= self.cur.data:
                new = node(None)
                new.left = self.cur
                new.right = node(data)
                self.cur = new
            else:
                new = node(data)
                new.left = self.cur
                self.cur = new
    def prints(self, cur):
        if cur:
            self.prints(cur.left)
            self.prints(cur.right)
            print(cur.data, end=" ")
            

def main():
    my_str = "BCCABBDDAECCBBAEDDCC"
    d = defaultdict(int)
    for i in my_str:
        d[i] += 1
    d_sorted = dict(sorted(d.items(), key=lambda x: x[1]))
    print(d_sorted)
    l = tree()
    for char, key in d_sorted.items():
        l.create(key)
    l.prints(l.cur)

main()
