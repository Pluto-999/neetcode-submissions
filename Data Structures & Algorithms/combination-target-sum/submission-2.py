class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result = []
        current = []

        def search(index):
            if sum(current) == target and current not in result:
                result.append(current[:])
                return
            elif sum(current) > target or index >= len(nums):
                return

            current.append(nums[index])
            search(index)
            current.pop()
            search(index + 1)

        search(0)
        return result

