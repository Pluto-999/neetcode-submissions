class Solution:
    def numDecodings(self, s: str) -> int:
        
        cache = {}
        
        def recurse(index):
            if index in cache: return cache[index]
            
            if index >= len(s): return 1
            
            one_num = s[index:index + 1]
            two_num = s[index:index + 2]
            one_num_res, two_num_res = 0, 0

            if int(one_num) != 0: 
                one_num_res = recurse(index + 1)
            if two_num[0] != "0" and index != len(s) - 1 and int(two_num) >= 1 and int(two_num) <= 26:
                two_num_res = recurse(index + 2)

            cache[index] = one_num_res + two_num_res
            return one_num_res + two_num_res

        return recurse(0)