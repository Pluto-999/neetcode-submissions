class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        result = []
        lowest, highest = intervals[0][0], intervals[0][1]

        for i in range(1, len(intervals)):
            (num1, num2) = intervals[i]

            if num1 <= highest:
                highest = max(num2, highest)
            else:
                result.append([lowest, highest])
                lowest = intervals[i][0]
                highest = intervals[i][1]

        result.append([lowest, highest])

        return result