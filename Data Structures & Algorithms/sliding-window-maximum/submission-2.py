class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        result = []
        
        heap = []
        for i in range(k):
            heapq.heappush_max(heap, (nums[i], i))

        result.append(heap[0][0])

        for i in range(k, len(nums)):
            heapq.heappush_max(heap, (nums[i], i))
            left_index = i - k
            while heap[0][1] <= left_index: # heap[0] gets top element then [1] gets 2nd item in pair (index)
                heapq.heappop_max(heap)
            result.append(heap[0][0])

        return result