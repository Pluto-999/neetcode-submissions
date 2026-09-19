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
            # if not node or (not node.left and not node.right): return 0
            if not node: return 0
            if not node.left and not node.right: return 1

            left_length = recurse(node.left)
            right_length = recurse(node.right)

            self.result = max(self.result, left_length + right_length )

            return 1 + max(left_length, right_length)

            # nodes_length = 1 + max(recurse(node.left), recurse(node.right))
            # self.result = max(self.result, nodes_length)
            # return nodes_length

        recurse(root)
        return self.result