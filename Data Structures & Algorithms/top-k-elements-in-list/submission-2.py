class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        nums_dict = dict()

        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
        
        heap = []

        for key, value in nums_dict.items():
            heapq.heappush(heap, (value, key))
            if len(heap) > k:
                heapq.heappop(heap)

        result = []

        while len(heap) > 0:
            (count, num) = heapq.heappop(heap)
            result.append(num)

        return result