class node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

class bst:
    def __init__(self):
        self.root=None
    
    def create(self,data):
        if self.root is None:
            self.root=node(data)
        else:
            self.recursive(self.root,data)
    
    def recursive(self,cur_node,value):
        if value<=cur_node.data:
            if cur_node.left is None:
                cur_node.left=node(value)
            else:
                self.recursive(cur_node.left,value)
        else:
            if cur_node.right is None:
                cur_node.right =node(value)
            else:
                self.recursive(cur_node.right,value)
    def inorder(self):
        return self.inorder1(self.root)

    def inorder1(self,root):
        if root:
            self.inorder1(root.left)
            print(root.data,end=" ")
            self.inorder1(root.right)
    
    def preorder(self):
        return self.preorder1(self.root)
    def preorder1(self,root):
        if root:
            print(root.data,end=" ")
            self.preorder1(root.left)
            self.preorder1(root.right)
    
    def postorder(self):
        return self.postorder1(self.root)
    
    def postorder1(self,root):
        if root:
            self.postorder1(root.left)
            self.postorder1(root.right)
            print(root.data,end=" ")


bst1 = bst()
data = [8, 3, 10, 1, 6, 14, 4, 7, 13]
for value in data:
    bst1.create(value)
print(" INITIAL NODE AND VALUEs")
print(data)
print(" ")
print("Inorder Traversal:")
bst1.inorder()  
print(" ")           
print("Pre-order Traversal:")
bst1.preorder()
print(" ")
print("Post order traversal") 
bst1.postorder()