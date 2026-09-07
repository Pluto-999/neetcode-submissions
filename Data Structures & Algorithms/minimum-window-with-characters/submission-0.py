class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        t_chars = {}

        for char in t:
            if char in t_chars:
                t_chars[char] += 1
            else:
                t_chars[char] = 1

        result = " " * 10**5

        left, right, s_chars = 0, 0, {}

        while right < len(s):

            char = s[right]

            if char in t_chars:
                if char in s_chars:
                    s_chars[char] += 1
                else:
                    s_chars[char] = 1

            if (right - left) + 1 < len(t):
                right += 1
                continue


            valid_substring = True

            for key, value in t_chars.items():
                if key not in s_chars or value > s_chars[key]:
                    valid_substring = False

            # begin shrinking here ??

            while left <= right and valid_substring:
                new_string = s[left : right + 1]
                if len(new_string) < len(result):
                    result = new_string
                if s[left] in s_chars:
                    s_chars[s[left]] -= 1
                left += 1
                for key, value in t_chars.items():
                    if key not in s_chars or value > s_chars[key]:
                        valid_substring = False


            right += 1

        if result == (" " * 10 ** 5):
            return ""
        else:
            return result