class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        def rob(nums):
            if len(nums) == 1:
                return nums[0]
            if len(nums) == 2:
                return max(nums[0], nums[1])

            dp = [0] * len(nums)

            dp[0] = nums[0]
            dp[1] = nums[1]

            for i in range(2, len(nums)):
                max_val = 0
                for j in range(i - 2, -1, -1):
                    max_val = max(max_val, dp[j])
                dp[i] = max(dp[i - 1], max_val + nums[i])

            return dp[-1]

        
        return max(rob(nums[:-1]), rob(nums[1:]))