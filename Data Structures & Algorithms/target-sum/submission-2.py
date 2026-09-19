class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        cache = {}
        
        def recurse(current, i):
            if (current, i) in cache: return cache[(current, i)]
            
            if i == len(nums) and current == target: return 1
            elif i == len(nums) and current != target: return 0

            cache[(current, i)] = recurse(current - nums[i], i + 1) + recurse(current + nums[i], i + 1)
            return cache[(current, i)]

        return recurse(0, 0)
    