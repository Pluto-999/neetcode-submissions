# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # if not root or (not root.left and not root.right): return True
        # if (
        #     (root.left and not root.right) or 
        #     (not root.left and root.right) or
        #     (root.left.val != root.right.val)
        # ):
        #     return False
        # else:
        #     return self.isSymmetric(root.left) and self.isSymmetric(root.right)



        def helper(left_node, right_node):
            if not left_node and not right_node: return True
            if (
                (not left_node and right_node) or
                (left_node and not right_node) or
                (left_node.val != right_node.val) or
                (left_node.left and not left_node.right and right_node.left and not right_node.right) or
                (not left_node.left and left_node.right and not right_node.left and right_node.right)
            ):
                return False
            else:
                return helper(left_node.left, right_node.right) and helper(left_node.right, right_node.left)


        return helper(root.left, root.right)