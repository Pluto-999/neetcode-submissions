class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        my_dict = {}

        for index, num in enumerate(nums):
            to_find = target - num
            if to_find in my_dict:
                return [my_dict[to_find], index]
            else:
                my_dict[num] = index

        return []
            