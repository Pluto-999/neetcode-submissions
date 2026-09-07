class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = {}
        
        def recurse(amount, index):
            
            if (amount, index) in dp:
                return dp[(amount, index)]
            
            if index == len(nums):
                if amount == target:
                    return 1
                else:
                    return 0

            result = recurse(amount - nums[index], index + 1) + recurse(amount + nums[index], index + 1)

            dp[(amount, index)] = result

            return result

        return recurse(0, 0)