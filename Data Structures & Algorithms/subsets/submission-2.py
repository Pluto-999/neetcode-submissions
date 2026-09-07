class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        curr = []
        def recurse(index):
            if index == len(nums):
                result.append(curr.copy())
                return
            # choose index
            curr.append(nums[index])
            recurse(index + 1)
            curr.pop()
            # skip index
            recurse(index + 1)
        recurse(0)
        return result