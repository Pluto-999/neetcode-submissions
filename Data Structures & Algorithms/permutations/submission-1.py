class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        def recurse(current, included):
            if len(current) == len(nums):
                result.append(current[:])
                return

            for i in range(len(nums)):
                if i in included: continue
                included.add(i)
                current.append(nums[i])
                recurse(current, included)
                included.remove(i)
                current.pop()
            
        recurse([], set())
        return result