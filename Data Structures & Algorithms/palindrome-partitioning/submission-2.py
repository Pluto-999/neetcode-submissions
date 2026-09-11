class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def is_palindrome(string):
            left, right = 0, len(string) - 1
            
            while left <= right:
                if string[left] != string[right]: return False
                left += 1
                right -= 1
            
            return True

        
        def recurse(i, current):
            if i >= len(s):
                result.append(current[:])
                return

            for j in range(i + 1, len(s) + 1):
                substr = s[i:j]
                if is_palindrome(substr):
                    current.append(substr)
                    recurse(j, current)
                    current.pop()
                    

        result = []
        recurse(0, [])
        return result