class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1

        result = 0

        while i < j:
            first_num = heights[i]
            second_num = heights[j]
            total = min(first_num, second_num) * abs(i - j)
            result = max(result, total)
            if first_num <= second_num:
                i += 1
            else:
                j -= 1

        return result