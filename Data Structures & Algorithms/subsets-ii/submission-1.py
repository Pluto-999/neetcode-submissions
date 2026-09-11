class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def recurse(i, current):
            if i == len(nums):
                result.append(current[:])
                return
            
            current.append(nums[i])
            recurse(i + 1, current)
            current.pop()
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            recurse(i + 1, current)

        result = []
        recurse(0, [])
        return result