class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        cache = {}

        def recurse(current):
            if current == amount:
                return 0
            if current > amount:
                return float("inf")
            if current in cache:
                return cache[current]

            best = float("inf")
            for coin in coins:
                result = recurse(current + coin)
                best = min(best, result + 1)

            cache[current] = best
            return best

        answer = recurse(0)
        return answer if answer != float("inf") else -1


        