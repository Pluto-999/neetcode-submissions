class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, result, seen = 0, 0, 0, set()

        while right < len(s):
            right_char = s[right]

            while right_char in seen and left <= right:
                seen.remove(s[left])
                left += 1

            seen.add(right_char)
            right += 1
            result = max(result, right - left)

        return max(result, right - left)