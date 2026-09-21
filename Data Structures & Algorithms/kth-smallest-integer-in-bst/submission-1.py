# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.in_order = []

        def search(node):
            if not node: return

            search(node.left)
            self.in_order.append(node.val)
            search(node.right)

        search(root)
        return self.in_order[k - 1]