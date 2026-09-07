# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        

        def helper(root, highest):
            if not root:
                return 0

            if root.val >= highest:
                highest = root.val
                return 1 + helper(root.left, highest) + helper(root.right, highest)
            else:
                return 0 + helper(root.left, highest) + helper(root.right, highest)
            


        return helper(root, root.val)