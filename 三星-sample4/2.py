# Example usage of the TreeNode class and Solution class

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(
        self, root: 'TreeNode', nodes: 'List[TreeNode]'
    ) -> 'TreeNode':
        def dfs(root):
            if root is None or root.val in s:
                return root
            left, right = dfs(root.left), dfs(root.right)
            if left and right:
                return root
            return left or right

        s = {node.val for node in nodes}
        return dfs(root)

# Test Case
# Creating a simple binary tree
#        3
#       / \
#      5   1
#     / \ / \
#    6  2 0  8
#      / \
#     7   4

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

# Creating a list of nodes [5, 1, 4]
nodes_to_find = [root.left, root.right, root.left.right.right]

# Creating an instance of the Solution class
solution = Solution()

# Finding the lowest common ancestor
result = solution.lowestCommonAncestor(root, nodes_to_find)

# Expected output: The lowest common ancestor of nodes [5, 1, 4] is the node with value 3
print(result.val)  # Output should be 3
