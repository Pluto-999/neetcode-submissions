class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []

        def backtrack(index):

            if index >= len(nums):
                result.append(current.copy())
                return
        

            current.append(nums[index])
            backtrack(index + 1)
            current.pop()

            backtrack(index + 1)

        backtrack(0)

        return result