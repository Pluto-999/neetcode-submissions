class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        for i in range(len(stones)):
            stones[i] *= -1

        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones) * -1
            second = heapq.heappop(stones) * -1

            if second < first:
                new_val = first - second
                heapq.heappush(stones, new_val * -1)

        if len(stones) == 0:
            return 0
        else:
            return stones[0] * -1
        
