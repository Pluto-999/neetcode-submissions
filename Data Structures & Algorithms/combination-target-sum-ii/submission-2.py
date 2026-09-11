class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()

        def recurse(i, current, total):
            if total == target:
                result.append(current[:])
                return
            if i >= len(candidates) or total > target: return

            current.append(candidates[i])
            recurse(i + 1, current, total + candidates[i])
            current.pop()
            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            recurse(i + 1, current, total)

        result = []
        recurse(0, [], 0)
        return result