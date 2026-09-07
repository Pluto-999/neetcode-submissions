class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        curr = []
        def recurse(index, total):
            if total == target:
                result.append(curr.copy())
                return
            elif total > target or index >= len(nums):
                return
            # choose number
            curr.append(nums[index])
            recurse(index, total + nums[index])
            curr.pop()
            # skip number
            recurse(index + 1, total)
        recurse(0, 0)
        return result 