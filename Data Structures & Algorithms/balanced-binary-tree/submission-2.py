# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)
        
        if (
            (left_height > right_height and right_height + 1 != left_height) or
            (right_height > left_height and left_height + 1 != right_height)
        ):
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        

    def get_height(self, root):
        if not root: return 0

        return 1 + max(self.get_height(root.left), self.get_height(root.right))