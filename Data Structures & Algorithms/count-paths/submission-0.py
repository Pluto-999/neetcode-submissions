class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for row in range(len(dp)):
            for col in range(len(dp[0])):
                if row == 0 and col == 0:
                    dp[row][col] = 1
                    continue
                
                total = 0
                above = col - 1
                left = row - 1

                if above >= 0:
                    total += dp[row][above]
                if left >= 0:
                    total += dp[left][col]

                dp[row][col] = total

        
        return dp[-1][-1]
