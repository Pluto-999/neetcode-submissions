class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) <= 1:
            return False

        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if top == "(" and char != ")" or top == "[" and char != "]" or top == "{" and char != "}":
                    return False
        
        if not stack: 
            return True
        else:
            return False