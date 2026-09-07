class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0

        my_set = set()

        result = 0

        for right, char in enumerate(s):
            while char in my_set:
                my_set.remove(s[left])
                left += 1
            my_set.add(char)
            result = max(result, right - left + 1)

        return result