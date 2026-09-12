# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # this function just traverses the tree and checks for subtree for every single node in this tree

        if not root: return False

        return (
            self.check_identical(root, subRoot) or 
            self.isSubtree(root.left, subRoot) or 
            self.isSubtree(root.right, subRoot)
        )
        

    # this function only returns true if both trees are exactly identical
    def check_identical(self, root, subRoot):
            if not root and not subRoot: return True
            if not root or not subRoot: return False
            if root and subRoot and root.val != subRoot.val: return False

            return (
                self.check_identical(root.left, subRoot.left) and 
                self.check_identical(root.right, subRoot.right)
            )
