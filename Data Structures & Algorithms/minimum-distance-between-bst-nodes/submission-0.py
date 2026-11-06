# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        all_values = []
        

        def search(self, node):
            if not node: return
            all_values.append(node.val)
            search(self, node.left)
            search(self, node.right)

        search(self, root)
        
        all_values.sort()
        
        result = float("inf")
        for i in range(1, len(all_values)):
            result = min(result, all_values[i] - all_values[i - 1])
        return result

        # queue = deque()
        # queue.append(root)

        # result = float("inf")

        # while queue:
        #     node = queue.popleft()
        #     if node.left:
        #         result = min(result, node.val - node.left.val)
        #         queue.append(node.left)
        #     elif node.right:
        #         result = min(result, node.right.val - node.val)
        #         queue.append(node.right)
        
        # return result