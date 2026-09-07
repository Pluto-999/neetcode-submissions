# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.list = []
        self.inOrderHelper(root)

        return self.list[k - 1]


    def inOrderHelper(self, root):
        if not root:
            return

        if root.left:
            self.inOrderHelper(root.left)
        self.list.append(root.val)
        if root.right:
            self.inOrderHelper(root.right)