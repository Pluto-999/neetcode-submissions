# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # if not root and not subRoot: return True
        # if not root or not subRoot: return False
        # if root and subRoot and root.val != subRoot.val: return False

        # # 3 conditions ...
        # # 1. when the root and subroot match, then the left subtree and right subtree of both root and subroot also need to match
        # # 2. when the root and subroot don't match, then check the left subtree of root (same subroot)
        # # 3. when the root and subroot don't match, then also check the right subtree of root (same subroot)


        # return (
        #     (root.val == subRoot.val and
        #     self.isSubtree(root.left, subRoot.left) and
        #     self.isSubtree(root.right, subRoot.right)) or
        #     self.isSubtree(root.left, subRoot) or
        #     self.isSubtree(root.right, subRoot)
        # )



        

        # at this point, we need to start seeing if the trees are completely identical 
        
        # result = False
        
        # if root.val == subRoot.val:
        #     result = result or self.check_identical(root, subRoot)
        # else:
        #     result = result or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        
        if not root: return False

        return self.check_identical(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        # return result

    def check_identical(self, root, subRoot):
            if not root and not subRoot: return True
            if not root or not subRoot: return False
            if root and subRoot and root.val != subRoot.val: return False

            return self.check_identical(root.left, subRoot.left) and self.check_identical(root.right, subRoot.right)
