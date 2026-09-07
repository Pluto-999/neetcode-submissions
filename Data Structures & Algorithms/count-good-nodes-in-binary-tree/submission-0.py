# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        highest = root.val

        return self.helper(root, highest)


    def helper(self, root, highest):
        if not root:
            return 0

        if root.val >= highest:
            return 1 + self.helper(root.left, root.val) + self.helper(root.right, root.val)
        else:
            return 0 + self.helper(root.left, highest) + self.helper(root.right, highest)