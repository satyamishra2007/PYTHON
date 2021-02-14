class BinarySearchTree:

    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def add_child(self,new_val):
        new_node =  BinarySearchTree(new_val)
        if new_val == self.val:
            return
        if new_val < self.val:
            if self.left:
                self.left.add_child(self.left)
            else:
                self.left = new_node
        if new_val > self.val:
            if self.right:
                self.right.add_child(self.right)
            else:
                self.right = new_node

    def inorder_traversal(self):
        tree_lst = []
        if self.left:
            tree_lst += self.left.inorder_traversal()
        tree_lst.append(self.val)
        if self.right:
            tree_lst += self.right.inorder_traversal()
        return tree_lst

    def preorder_traversal(self):
        tree_lst = []
        tree_lst.append(self.val)
        if self.left:
            tree_lst += self.left.inorder_traversal()
        if self.right:
            tree_lst += self.right.inorder_traversal()
        return tree_lst

    def postorder_traversal(self):
        tree_lst = []
        if self.left:
            tree_lst += self.left.inorder_traversal()
        if self.right:
            tree_lst += self.right.inorder_traversal()
        tree_lst.append(self.val)
        return tree_lst


# lst = [1,12,13,5,7,8,10]
# root = BinarySearchTree(lst[0])
# for i in lst[1:]:
#     root.add_child(i)

root = BinarySearchTree(10)
root.add_child(15)
root.add_child(6)
print("In   order Traversal:",root.inorder_traversal())
print("Pre  order Traversal:",root.preorder_traversal())
print("post order Traversal:",root.postorder_traversal())









