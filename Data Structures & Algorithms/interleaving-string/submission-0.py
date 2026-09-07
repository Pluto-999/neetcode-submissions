class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        cache = {}

        def recurse(s1_ptr, s2_ptr):
            if (s1_ptr, s2_ptr) in cache:
                return cache[(s1_ptr, s2_ptr)]

            s3_ptr = s1_ptr + s2_ptr

            if s1_ptr == len(s1) and s2_ptr == len(s2) and s3_ptr == len(s3):
                return True

            s1_result, s2_result = False, False

            if s1_ptr < len(s1) and s3_ptr < len(s3) and s1[s1_ptr] == s3[s3_ptr]:
                s1_result = recurse(s1_ptr + 1, s2_ptr)
            if s2_ptr < len(s2) and s3_ptr < len(s3) and s2[s2_ptr] == s3[s3_ptr]:
                s2_result = recurse(s1_ptr, s2_ptr + 1)

            cache[(s1_ptr, s2_ptr)] = False or s1_result or s2_result

            return cache[(s1_ptr, s2_ptr)]
            

        return recurse(0, 0)