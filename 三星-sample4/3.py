# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def insert_into_bst(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.val:
        root.left = insert_into_bst(root.left, value)
    else:
        root.right = insert_into_bst(root.right, value)
    return root

# Given array
array = [2, 3, 4, 6, 1, 7]

# Initialize the root of the tree with the first element of the array
root = TreeNode(array[0])

# Insert the remaining elements into the BST
for value in array[1:]:
    insert_into_bst(root, value)

# Now, the binary search tree should look like:
#        2
#       / \
#      1   3
#         / \
#        4   6
#             \
#              7

print(root.right.right.val)