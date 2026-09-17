class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0] * n for _ in range(m)]

        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                up, left = i - 1, j - 1
                if up >= 0: dp[i][j] += dp[up][j]
                if left >= 0: dp[i][j] += dp[i][left]

        return dp[-1][-1]