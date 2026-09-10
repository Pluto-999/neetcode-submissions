class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def recurse(i, current):
            if i == len(nums):
                result.append(current[:])
                return
            
            current.append(nums[i])
            recurse(i + 1, current)
            current.pop()
            recurse(i + 1, current)

        result = []
        recurse(0, [])
        return result