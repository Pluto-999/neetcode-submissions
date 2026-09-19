# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.result = 0

        def recurse(node):
            if not node: return 0

            left_length = recurse(node.left)
            right_length = recurse(node.right)

            self.result = max(self.result, left_length + right_length)

            return 1 + max(left_length, right_length)

        recurse(root)
        return self.result