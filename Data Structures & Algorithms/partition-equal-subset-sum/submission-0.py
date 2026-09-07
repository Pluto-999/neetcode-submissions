class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        cache = {}

        def recurse(index, sub1, sub2):
            
            if (sub1, sub2) in cache:
                return cache[(sub1, sub2)]

            if index == len(nums):
                if sub1 == sub2:
                    return True
                else:
                    return False

            # we go thru each element and can either put it in sub1 or sub2
            new_sub1 = sub1 + nums[index]
            new_sub2 = sub2 + nums[index]
            add_sub1 = recurse(index + 1, new_sub1, sub2)
            add_sub2 = recurse(index + 1, sub1, new_sub2)
            cache[(new_sub1, sub2)] = add_sub1
            cache[(sub1, new_sub2)] = add_sub2

            return add_sub1 or add_sub2


        return recurse(0, 0, 0)