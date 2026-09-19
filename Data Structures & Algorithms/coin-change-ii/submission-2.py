class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        cache = {}

        def recurse(current, i):
            if (current, i) in cache: return cache[(current, i)]
            
            if current == amount: return 1
            if current > amount or i >= len(coins): return 0

            cache[(current, i)] = recurse(current + coins[i], i) + recurse(current, i + 1)
            return cache[(current, i)]

        return recurse(0, 0)