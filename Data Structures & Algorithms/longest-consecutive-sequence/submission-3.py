class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        
        nums_set = set(nums)
        nums = list(nums_set)

        nums.sort()

        result = 1
        counter = 1

        for i in range(1, len(nums)):
            prev, curr = nums[i - 1], nums[i]
            if prev + 1 == curr:
                counter += 1
            else:
                result = max(result, counter)
                counter = 1 

        return max(result, counter)