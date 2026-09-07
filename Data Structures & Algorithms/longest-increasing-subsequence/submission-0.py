class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            max_value = 1
            for j in range(i, -1, -1):
                if nums[i] > nums[j]:
                    max_value = max(max_value, dp[j] + 1)

                dp[i] = max_value

        return max(dp)