class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        cache = {}

        def recurse(ptr1, ptr2):
            if (ptr1, ptr2) in cache: return cache[(ptr1, ptr2)]
            
            if ptr1 >= len(text1) or ptr2 >= len(text2): return 0

            if text1[ptr1] == text2[ptr2]: 
                return 1 + recurse(ptr1 + 1, ptr2 + 1)
            else:
                result = max(recurse(ptr1 + 1, ptr2), recurse(ptr1, ptr2 + 1))
                cache[(ptr1, ptr2)] = result
                return result

        return recurse(0, 0)