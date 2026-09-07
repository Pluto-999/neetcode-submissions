# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # self.my_set = set()
        # self.my_set.add(root.val)
        
        self.result = 1

        self.helper(root.left, root.val)
        self.helper(root.right, root.val)

        return self.result
        

    def helper(self, subTree, highest_value):
        if not subTree:
            return

        if subTree.val >= highest_value:
            self.result += 1
            self.helper(subTree.left, subTree.val)
            self.helper(subTree.right, subTree.val)
        else:
            self.helper(subTree.left, highest_value)
            self.helper(subTree.right, highest_value)        
