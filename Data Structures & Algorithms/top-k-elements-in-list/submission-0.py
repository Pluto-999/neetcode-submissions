class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        my_dict = {}

        for num in nums:
            if num in my_dict:
                my_dict[num] += 1
            else:
                my_dict[num] = 1

        heap = []
        
        for key, value in my_dict.items():
            heapq.heappush(heap, (value * - 1, key))

        result = []

        while k > 0:
            value, key = heapq.heappop(heap)
            result.append(key)
            k -= 1

        return result
