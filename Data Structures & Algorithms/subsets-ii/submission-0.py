class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []

        nums.sort()

        def recurse(index):
            if index >= len(nums):
                result.append(current[:])
                return

            current.append(nums[index])
            recurse(index + 1)
            
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1

            current.pop()
            recurse(index + 1)

        recurse(0)
        return result