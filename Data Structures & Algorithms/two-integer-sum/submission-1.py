class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = dict()

        for i, num in enumerate(nums):         
            num_to_check = target - num
            
            if num_to_check in nums_dict:
                return [nums_dict[num_to_check], i]
            else:
                nums_dict[num] = i
