class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left_product, right_product = [1] * len(nums), [1] * len(nums)
        left_res, right_res = 1, 1

        for i in range(1, len(nums)):
            left_res = left_res * nums[i - 1]
            left_product[i] = left_res

        for j in range(len(nums) - 2, -1, -1):
            right_res = right_res * nums[j + 1 ]
            right_product[j] = right_res

        result = []

        for k in range(len(nums)):
            result.append(left_product[k] * right_product[k])

        return result
