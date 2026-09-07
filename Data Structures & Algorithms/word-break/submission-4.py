class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        cache = {len(s): True}

        def recurse(index):

            if index in cache:
                return cache[index]

            for word in wordDict:
                if index + len(word) <= len(s) and s[index: index + len(word)] == word:
                    if recurse(index + len(word)):
                        cache[index] = True
                        return True
                
            cache[index] = False
            return False

        
        return recurse(0)