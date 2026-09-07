class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        my_dict = {}

        def recurse(amount, index):
            if amount < 0 or index >= len(coins):
                return 0
            
            if (amount, index) in my_dict:
                return my_dict[(amount, index)]

            if amount == 0:
                return 1

            result = 0

            # choose the coin
            choose_coin = recurse(amount - coins[index], index)

            # don't choose the coin and move on 
            dont_choose_coin = recurse(amount, index + 1)

            result = choose_coin + dont_choose_coin

            my_dict[(amount, index)] = result

            return result

        return recurse(amount, 0)