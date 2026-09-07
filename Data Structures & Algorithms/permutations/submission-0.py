class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        current = []

        def recurse():
            
            if len(current) == len(nums):
                result.append(current[:])
                return
            
            for num in nums:
                if num not in current:
                    current.append(num)
                    recurse()
                    current.pop()

        
        recurse()
        return result