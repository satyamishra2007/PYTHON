"""

"""
"""
Structure: 

An AVL tree is a self-balancing binary search tree in which 
the heights of the two child subtrees of any node differ by at most one.


Properties:

Balance factor (height difference between left and right subtrees) of each node is either -1, 0, or 1.
The tree is automatically balanced after every insertion or deletion operation.

Operations:
- All basic binary search tree operations (searching, insertion, deletion) 
- are supported with an additional constraint on balancing.


Advantages:
- Guarantees logarithmic height and, thus, O(log n) time complexity for all operations.
- Efficient for dynamic sets requiring frequent insertions and deletions.
"""


class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def balance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotate_right(self, y):
        x = y.left
        T = x.right

        x.right = y
        y.left = T

        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        return x

    def rotate_left(self, x):
        y = x.right
        T = y.left

        y.left = x
        x.right = T

        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def insert(self, root, key):
        if root is None:
            return AVLNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        # Left Left Case
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)

        # Right Right Case
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)

        # Left Right Case
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Right Left Case
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.key, end=' ')
            self.inorder_traversal(root.right)

    def search(self, root, key):
        if root is None or root.key == key:
            return root is not None
        elif key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)


# Example usage:
avl_tree = AVLTree()
keys = [10, 5, 15, 2, 7, 12, 17, 1, 3, 6, 8]
for key in keys:
    avl_tree.root = avl_tree.insert(avl_tree.root, key)

print("Inorder Traversal:", end=' ')
avl_tree.inorder_traversal(avl_tree.root)
print()

print("Search for key 7:", avl_tree.search(avl_tree.root, 7))

"""

Example:
We'll insert the following keys into an AVL tree: 10, 5, 15, 2, 7, 12, 17, 1, 3, 6, 8.

Step 1: Insert 10 (Root)

     10
Since this is the first node, it becomes the root of the AVL tree.

Step 2: Insert 5
     10
    /
   5
The left subtree's height is now 1, and the right subtree's height is 0. The balance factor of the root node is +1.

Step 3: Insert 15

     10
    /  \
   5   15
The right subtree's height is now 1, and the left subtree's height remains 1. The balance factor of the root node is 0.

Step 4: Insert 2
markdown
Copy code
     10
    /  \
   5   15
  /
 2
The left subtree's height increases to 2, and the right subtree's height remains 1. The balance factor of the root node is -1.

Step 5: Rotate Right (Single Rotation)
Perform a right rotation at node 10 to rebalance the tree.

markdown
Copy code
      5
     / \
    2   10
        \
        15
The balance factor of node 5 is now 0, and the balance factor of node 10 is 0.

Step 6: Insert 7
markdown
Copy code
      5
     / \
    2   10
       / \
      7  15
The balance factor of node 5 is still 0, and the balance factor of node 10 is -1.

Step 7: Rotate Left-Right (Double Rotation)
Perform a left rotation at node 10, then a right rotation at node 5.

markdown
Copy code
      7
     / \
    5   10
   /   / \
  2   8  15
The balance factor of node 7 is now 0, the balance factor of node 5 is 0, and the balance factor of node 10 is 0.

Step 8: Insert 12
markdown
Copy code
      7
     / \
    5   10
   /   / \
  2   8  15
       \
       12
The balance factor of node 7 is 0, the balance factor of node 5 is 0, and the balance factor of node 10 is -1.

Step 9: Rotate Right (Single Rotation)
Perform a right rotation at node 10.

markdown
Copy code
      7
     / \
    5   12
   /   / \
  2   8  15
       \
       10
The balance factor of node 7 is now 0, the balance factor of node 5 is 0, and the balance factor of node 12 is 0.

Step 10: Insert 17
markdown
Copy code
      7
     / \
    5   12
   /   / \
  2   8  15
       \   \
       10   17
The balance factor of node 7 is 0, the balance factor of node 5 is 0, and the balance factor of node 12 is -1.

Step 11: Rotate Left-Right (Double Rotation)
Perform a left rotation at node 12, then a right rotation at node 7.

markdown
Copy code
      10
     /  \
    7   15
   / \    \
  5   8   17
 / \
2   6
The AVL tree is now balanced, and all balance factors are 0.


"""
