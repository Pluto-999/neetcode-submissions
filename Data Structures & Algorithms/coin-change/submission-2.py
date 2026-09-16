class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        cache = {}

        def recurse(curr_total):
            if curr_total in cache: return cache[curr_total]

            if curr_total == amount: return 0
            if curr_total > amount: return float("inf")

            lowest = float("inf")

            for coin in coins:
                lowest = min(lowest, 1 + recurse(curr_total + coin))

            cache[curr_total] = lowest
            return lowest

        result = recurse(0)
        return result if result != float("inf") else -1