class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = [0] * (len(s) + 1)
        dp[0] = 1 # empty string - 1 option
        dp[1] = 1 if s[0] != '0' else 0 # first number - also 1 option IF not 0 !!

        for i in range(2, len(dp)):
            one_digit = int(s[i - 1])
            two_digit = int(s[i - 2:i])

            if 0 < one_digit <= 9:
                dp[i] += dp[i - 1]

            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]

        return dp[-1]
            