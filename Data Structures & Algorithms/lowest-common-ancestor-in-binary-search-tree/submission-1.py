# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # if root.left and root.right and (root.left.val == p.val and root.right.val == q.val or 

        # if (
        #     root.left and root.right and
        #     (
        #         (root.left.val == p.val and root.right.val == q.val) or
        #         (root.left.val == q.val and root.right.val == p.val) or
        #         (root.val == p.val )
        #     )
        # )



        # if p.val > q.val:
        #     temp = p
        #     p = q
        #     q = temp


        # recursive cases/looking to find the answer
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)

        # base cases/cases where we have found the answer
        elif root.val == p.val or root.val == q.val:
            return root
        elif (root.val > p.val and root.val < q.val) or (root.val < p.val and root.val > q.val):
            return root
    
        return None
    
