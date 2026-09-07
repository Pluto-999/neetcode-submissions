class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        def recurse(index, has_bought, total):
            if index >= len(prices):
                return total

            # when bought, we can sell (then go to index + 2) or skip the day
            if has_bought:
                sell = recurse(index + 2, not has_bought, total + prices[index])
                skip = recurse(index + 1, has_bought, total)
                return max(sell, skip)
            # when not bought, we can buy or skip the day
            else:
                buy = recurse(index + 1, not has_bought, total - prices[index])
                skip = recurse(index + 1, has_bought, total)
                return max(buy, skip)

        return recurse(0, False, 0)