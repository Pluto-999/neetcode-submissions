# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        return self.checkSubtree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def checkSubtree(self, root, subRoot):
        if (not root and not subRoot):
            return True
        elif (root and not subRoot) or (not root and subRoot):
            return False
        
        if root.val != subRoot.val:
            return False

        return self.checkSubtree(root.left, subRoot.left) and self.checkSubtree(root.right, subRoot.right)
        