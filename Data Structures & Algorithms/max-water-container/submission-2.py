class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        result = 0
        
        left, right = 0, len(heights) - 1

        while left < right:
            total = (right - left) * min(heights[left], heights[right])
            result = max(result, total)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return result