class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) == 1: return s

        result = ""
        max_len = 0


        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    if (right - left) + 1 > max_len:
                        max_len = right - left
                        result = s[left:right + 1]
                    left -= 1
                    right += 1
                else:
                    break
            
            left, right = i, i + 1
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    if right - left > max_len:
                        max_len = right - left
                        result = s[left:right + 1]
                    left -= 1
                    right += 1
                else:
                    break

        return result