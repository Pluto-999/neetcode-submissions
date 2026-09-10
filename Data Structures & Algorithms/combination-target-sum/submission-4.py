class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result = []

        def recurse(i, current, total):
            if total == target:
                result.append(current[:])
                return 
            elif total > target or i >= len(nums):
                return

            current.append(nums[i])
            recurse(i, current, total + nums[i])
            current.pop()
            recurse(i + 1, current, total)


        recurse(0, [], 0)
        return result