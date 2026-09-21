class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        cache = {}

        def recurse(i, current_max):
            if (i, current_max) in cache: return cache[(i, current_max)]
            
            if i == len(nums): return 0

            result = 0

            # pick and include (if possible)
            if nums[i] > current_max: result = max(result, 1 + recurse(i + 1, nums[i]))

            # don't pick and move on
            result = max(result, recurse(i + 1, current_max))

            cache[(i, current_max)] = result
            return result


        return recurse(0, float("-inf"))