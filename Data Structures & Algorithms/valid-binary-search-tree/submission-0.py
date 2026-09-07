# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result = []

        self.traversal(root, result)

        sorted_result = sorted(result)
        
        # Need to remove duplicates !
        my_set = set()
        new_sorted_result = []

        for num in sorted_result:
            if num not in my_set:
                new_sorted_result.append(num)
                my_set.add(num)

        if new_sorted_result == result:
            return True
        else:
            return False

    
    def traversal(self, root, result):
        if not root:
            return

        if root.left:
            self.traversal(root.left, result)
        result.append(root.val)
        if root.right:
            self.traversal(root.right, result)