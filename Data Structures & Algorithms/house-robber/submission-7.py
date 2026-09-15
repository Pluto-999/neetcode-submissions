class Solution:
    def rob(self, nums: List[int]) -> int:
        
        totals = [0] * len(nums)
        totals[0] = nums[0]

        for i in range(1, len(nums)):
            if i == 1: totals[i] = max(totals[i - 1], nums[i])
            else: totals[i] = max(totals[i - 1], nums[i] + totals[i - 2])

        return totals[-1]