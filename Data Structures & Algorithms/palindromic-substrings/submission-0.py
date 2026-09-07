class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        my_set = set()

        def palindrome(string):
            if len(string) == 0:
                return False
            if len(string) == 1:
                return True
            left = 0
            right = len(string) - 1
            while left < right:
                if string[left] != string[right]:
                    return False
                left += 1
                right -= 1
            my_set.add(string)
            return True

        for i in range(0, len(s)):
            for j in range(i, len(s)):
                if s[i:j+1] in my_set:
                    result += 1
                    continue
                if palindrome(s[i:j+1]):
                    result += 1
            

        return result