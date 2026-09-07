class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): return False
        
        s_dict = dict()
        for char in s:
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1

        for char in t:
            if char not in s_dict:
                return False
            
            s_dict[char] -= 1
            if s_dict[char] == 0:
                del s_dict[char]

        return len(s_dict) == 0