class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        j = 0
        result = 0
        for i in range(1, len(prices)):

            while prices[i] < prices[j]:
                j += 1

            if i == j:
                continue
            else:
                result = max(result, (prices[i] - prices[j]))


        return result