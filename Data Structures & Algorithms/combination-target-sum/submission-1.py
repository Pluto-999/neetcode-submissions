class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # our decision is: 
        # choose the number and recurse with same index
        # not choose the number and recurse with next index


        result = []
        current = []

        def recurse(index):
            if sum(current) == target:
                result.append(current.copy())
                return
            elif sum(current) > target or index >= len(nums):
                return
            
            current.append(nums[index])
            recurse(index)
            current.pop()
            recurse(index + 1)

        recurse(0)
        return result