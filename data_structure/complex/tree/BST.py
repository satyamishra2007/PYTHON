"""
Binary Search tree can have at max 2 child .(0 or 1 or 2). Its ordered and non duplicate(like set)
left   --> Holds smaller value than it's root
right  --> Holds larger value than it's root

"""
"""
A binary search tree (BST) is a binary tree data structure in which each node has at most two children 
(referred to as the left child and the right child), and the keys in the left subtree are less than 
the key in the root, while the keys in the right subtree are greater than the key in the root. 
BSTs support efficient search, insertion, and deletion operations.

"""


class BinarySearchTree:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def add_child(self, new_val):
        new_node = BinarySearchTree(new_val)

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

    # print left -> root -> right
    def inorder_traversal(self):

        tree_lst = []
        if self.left:
            tree_lst += self.left.inorder_traversal()
        tree_lst.append(self.val)

        if self.right:
            tree_lst += self.right.inorder_traversal()
        return tree_lst

    # print root -> left -> right
    def preorder_traversal(self):
        tree_lst = []
        tree_lst.append(self.val)
        if self.left:
            tree_lst += self.left.inorder_traversal()
        if self.right:
            tree_lst += self.right.inorder_traversal()
        return tree_lst

    # print left -> right -> root
    def postorder_traversal(self):
        tree_lst = []
        if self.left:
            tree_lst += self.left.inorder_traversal()
        if self.right:
            tree_lst += self.right.inorder_traversal()
        tree_lst.append(self.val)
        return tree_lst

    def search(self, data):
        if data == self.val:
            return True

        if data < self.val:
            if self.left:
                return self.left.search(data)
            else:
                return False

        if data > self.val:
            if self.right:
                return self.right.search(data)

            else:
                return False

    def find_max(self):
        if self.right is None:
            return self.val

        else:
            return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.val
        else:
            return self.left.find_min()

    def sum(self):
        sum = 0

        if self.left:
            sum += self.left.sum()
        sum += self.val

        if self.right:
            sum += self.right.sum()
        sum += self.val

        return sum
    # def delete_node(self,data):


# lst = [1,12,13,5,7,8,10]
# root = BinarySearchTree(lst[0])
# for i in lst[1:]:
#     root.add_child(i)

root = BinarySearchTree(10)
root.add_child(15)
root.add_child(6)
print("In   order Traversal:", root.inorder_traversal())
print("Pre  order Traversal:", root.preorder_traversal())
print("post order Traversal:", root.postorder_traversal())


"""
Search:

Average case: O(log n)
Worst case (unbalanced tree): O(n)
Insertion:

Average case: O(log n)
Worst case (unbalanced tree): O(n)
Deletion:

Average case: O(log n)
Worst case (unbalanced tree): O(n)
Inorder Traversal (printing elements in sorted order):

O(n)


"""