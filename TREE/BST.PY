class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.recursive(self.root, value)
            
    def recursive(self,cur_node,value):
        if value<=cur_node.data:
            if cur_node.left is None:
                cur_node.left=Node(value)
            else:
                self.recursive(cur_node.left,value)
        else:
            if cur_node.right is None:
                cur_node.right=Node(value)
            else:
                self.recursive(cur_node.right,value)
                
    def inorder_traversal(self):
        return self._inorder_traversal_recursive(self.root)

    def _inorder_traversal_recursive(self, current_node):
        if current_node is not None:
            self._inorder_traversal_recursive(current_node.left)
            print(current_node.data, end=" ")
            self._inorder_traversal_recursive(current_node.right)

bst = BinarySearchTree()
data = [8, 3, 10, 1, 6, 14, 4, 7, 13]
for value in data:
    bst.insert(value)

print("Inorder Traversal:")
bst.inorder_traversal()  