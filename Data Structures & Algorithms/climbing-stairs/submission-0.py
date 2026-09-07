class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [0] * (n + 1)

        def helper(n):
            if arr[n] != 0:
                return arr[n]
            elif n < 0:
                return 0
            elif n == 0:
                return 1
            else:
                arr[n] = helper(n - 1) + helper(n - 2)
                return arr[n]

        return helper(n)