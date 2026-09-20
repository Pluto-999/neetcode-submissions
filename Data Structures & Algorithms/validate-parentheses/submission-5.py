class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 == 1: return False

        stack = []
        
        for char in s:
            if char == "(" or char == "[" or char == "{": stack.append(char)
            elif char == ")" and len(stack) > 0 and stack[-1] == "(": stack.pop()
            elif char == "]" and len(stack) > 0 and stack[-1] == "[": stack.pop()
            elif char == "}" and len(stack) > 0 and stack[-1] == "{": stack.pop()
            else: return False


        return True if len(stack) == 0 else False