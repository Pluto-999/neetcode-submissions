class Solution:
    def rob(self, nums: List[int]) -> int:
        
        total_amount = [0] * len(nums)

        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        total_amount[-1] = nums[-1]
        total_amount[-2] = nums[-2]

        for i in range(len(total_amount) - 3, -1, -1):
            
            max_amount = 0
            for j in range(i + 2, len(total_amount)):
                
                max_amount = max(max_amount, total_amount[j])

            total_amount[i] = nums[i] + max_amount

        return max(total_amount[0], total_amount[1])