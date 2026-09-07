# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        self.max_helper(root)
        return self.result

    def depth_helper(self, root):
        if not root:
            return 0

        return 1 + max(self.depth_helper(root.left), self.depth_helper(root.right))

    def max_helper(self, root):
        if not root:
            return

        self.result = max(self.result, self.depth_helper(root.left) + self.depth_helper(root.right))

        self.max_helper(root.left)
        self.max_helper(root.right)
        