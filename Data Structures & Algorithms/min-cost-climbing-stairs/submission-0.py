class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        accumulate_cost = [0] * len(cost)

        accumulate_cost[-1] = cost[-1]
        accumulate_cost[-2] = cost[-2]

        for i in range(len(accumulate_cost) - 3, -1, -1):
            accumulate_cost[i] = cost[i] + min(accumulate_cost[i + 1], accumulate_cost[i + 2])

        return min(accumulate_cost[0], accumulate_cost[1])