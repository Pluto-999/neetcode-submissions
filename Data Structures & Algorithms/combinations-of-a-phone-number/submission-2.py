class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits) == 0: return []

        mapping = dict()
        mapping["2"] = ["a", "b", "c"]
        mapping["3"] = ["d", "e", "f"]
        mapping["4"] = ["g", "h", "i"]
        mapping["5"] = ["j", "k", "l"]
        mapping["6"] = ["m", "n", "o"]
        mapping["7"] = ["p", "q", "r", "s"]
        mapping["8"] = ["t", "u", "v"]
        mapping["9"] = ["w", "x", "y", "z"]
        
        
        def recurse(i, current):
            if i >= len(digits):
                result.append(current)
                return

            for letter in mapping[digits[i]]:
                new_current = current + letter
                recurse(i + 1, new_current)

        result = []
        recurse(0, "")
        return result