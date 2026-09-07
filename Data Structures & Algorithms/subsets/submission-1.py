class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        current = []

        def recurse(index):
            if index == len(nums):
                result.append(current[:])
                return
            
            current.append(nums[index])
            recurse(index + 1)
            current.pop()
            recurse(index + 1)

        recurse(0)
        return result