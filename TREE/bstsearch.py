class node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class bst:
    def __init__(self):
        self.root = None
    
    def create(self, data):
        if self.root is None:
            self.root = node(data)
        else:
            self.recursive(self.root, data)
    
    def recursive(self, cur_node, value):
        if value <= cur_node.data:
            if cur_node.left is None:
                cur_node.left = node(value)
            else:
                self.recursive(cur_node.left, value)
        else:
            if cur_node.right is None:
                cur_node.right = node(value)
            else:
                self.recursive(cur_node.right, value)
    
    def deletenode(self, val):
        if self.root is None:
            return
        else:
            self.root = self.deletechild(self.root, val)
    
    def deletechild(self, cur, val):
        if cur.data > val:
            cur.left = self.deletechild(cur.left, val)
        elif cur.data < val:
            cur.right = self.deletechild(cur.right, val)
        else:
            if cur.left is None:
                return cur.right
            if cur.right is None:
                return cur.left
            cur.data = self.findMin(cur.right)
            cur.right = self.deletechild(cur.right, cur.data)
        return cur
    def inorder(self):
        return self.inorder1(self.root)

    def inorder1(self, root):
        if root:
            self.inorder1(root.left)
            print(root.data, end=" ")
            self.inorder1(root.right)
    
    def findMin(self, root):
        while root.left is not None:
            root = root.left
        return root.data

bst1 = bst()
data = [8, 3, 10, 1, 6, 14, 4, 7, 13]
for value in data:
    bst1.create(value)
bst1.deletenode(13)

bst1.inorder()
