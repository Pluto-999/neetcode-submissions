class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        my_set = set()

        
        for index, num in enumerate(nums):
            i = 0
            j = len(nums) - 1

            while i < j:
                if i == index:
                    i += 1
                    continue
                if j == index:
                    j -= 1
                    continue

                total = num + nums[i] + nums[j]

                if total == 0:
                    to_add = [num, nums[i], nums[j]]
                    to_add.sort()
                    my_set.add(tuple(to_add))
                elif total < 0:
                    i += 1
                    continue
                else:
                    j -= 1
                    continue
                i += 1
                j -= 1
            
        result = []
        for item in my_set:
            result.append(list(item))

        return result