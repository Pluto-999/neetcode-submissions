class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        cache = {}

        def recurse(index):
            if index in cache: return cache[index]

            if index >= len(s): return True

            result = False

            for word in wordDict:
                word_len = len(word)
                if s[index:index + word_len] == word:
                    result = result or recurse(index + word_len)

            cache[index] = result
            return result

        return recurse(0)