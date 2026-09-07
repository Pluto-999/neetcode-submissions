class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        s_dict = {}
        t_dict = {}

        for letter in s:
            if letter in s_dict:
                s_dict[letter] = s_dict.get(letter) + 1
            else:
                s_dict[letter] = 1

        for letter in t:
            if letter in t_dict:
                t_dict[letter] = t_dict.get(letter) + 1
            else:
                t_dict[letter] = 1

        if len(s_dict) != len(t_dict):
            return False

        for key in s_dict:
            s_val = s_dict.get(key)
            t_val = t_dict.get(key)
            if s_val == None or t_val == None or s_val != t_val:
                return False

        return True