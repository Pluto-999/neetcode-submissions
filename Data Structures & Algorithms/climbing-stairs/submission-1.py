class Solution:
    def climbStairs(self, n: int) -> int:
        
        cache = {}

        def count(num):
            if num in cache: return cache[num]

            if num == 0: return 1
            elif num < 0: return 0
            else:
                total = count(num - 1) + count(num - 2)
                cache[num] = total
                return total

        return count(n)
        