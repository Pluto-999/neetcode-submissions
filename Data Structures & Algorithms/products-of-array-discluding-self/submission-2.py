class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zero_counter = 0
        for num in nums:
            if num:
                total *= num
            else:
                zero_counter +=  1
        if zero_counter > 1: return [0] * len(nums)

        result = [0] * len(nums)
        for index, num in enumerate(nums):
            if zero_counter: result[index] = 0 if num else total
            else: result[index] = total // num
        return result