class Solution:
    def isPalindrome(self, s: str) -> bool:
        to_check = []
        for char in s:
            if char.isalnum():
                to_check.append(char.lower())
        
        j = len(to_check) - 1
        for i in range(0, len(to_check) // 2):
            left = to_check[i]
            right = to_check[j]
            if left != right:
                return False
            j -= 1
        
        return True