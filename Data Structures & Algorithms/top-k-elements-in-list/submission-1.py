class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        nums_dict = dict()

        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
        
        heap = []
        result = []

        for key, value in nums_dict.items():
            heapq.heappush_max(heap, (value, key))

        while k > 0:
            (count, num) = heapq.heappop_max(heap)
            result.append(num)
            k -= 1

        return result