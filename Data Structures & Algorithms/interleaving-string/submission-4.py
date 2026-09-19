class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        cache = {}

        def recurse(ptr1, ptr2, ptr3):
            if (ptr1, ptr2, ptr3) in cache: return cache[(ptr1, ptr2, ptr3)]
            
            if ptr1 >= len(s1) and ptr2 >= len(s2) and ptr3 >= len(s3):
                return True

            result = False

            if ptr1 < len(s1) and ptr3 < len(s3) and s1[ptr1] == s3[ptr3]:
                result = result or recurse(ptr1 + 1, ptr2, ptr3 + 1)
            if ptr2 < len(s2) and ptr3 < len(s3) and s2[ptr2] == s3[ptr3]: 
                result = result or recurse(ptr1, ptr2 + 1, ptr3 + 1)
            
            cache[(ptr1, ptr2, ptr3)] = result

            return result

        return recurse(0, 0, 0)