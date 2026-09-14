# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, highest):
            if not root: return

            if root.val >= highest:
                self.result += 1
                highest = root.val

            dfs(root.left, highest)
            dfs(root.right, highest)


        self.result = 0
        dfs(root, root.val)
        return self.result
