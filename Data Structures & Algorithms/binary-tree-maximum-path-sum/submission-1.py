# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = float("-inf")

        def recurse(node):
            if not node: 
                return 0

            left_subtree_total = max(recurse(node.left), 0)
            right_subtree_total = max(recurse(node.right), 0)

            total = node.val + left_subtree_total + right_subtree_total
            self.result = max(total, self.result)
            return max(node.val + left_subtree_total, node.val + right_subtree_total)

        recurse(root)
        return self.result