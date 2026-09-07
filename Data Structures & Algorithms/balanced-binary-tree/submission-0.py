# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        left_subtree = self.depth_helper(root.left)
        right_subtree = self.depth_helper(root.right)

        if right_subtree + 1 < left_subtree or left_subtree + 1 < right_subtree:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth_helper(self, root):
        if not root:
            return 0

        return 1 + max(self.depth_helper(root.left), self.depth_helper(root.right))
        