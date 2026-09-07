class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distances = []

        for coords in points:
            x = coords[0]
            y = coords[1]
            distance = math.sqrt(x**2 + y**2)
            distances.append((distance, [x, y]))

        heapq.heapify(distances)
        
        result, counter = [], 0

        while counter < k:
            result.append(heapq.heappop(distances)[1])
            counter += 1

        return result