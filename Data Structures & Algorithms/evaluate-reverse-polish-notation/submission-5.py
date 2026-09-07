class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        stack.append(int(tokens[0]))

        for index in range(1, len(tokens)):
            token = tokens[index]
            if not (token == "+") and not (token == "-") and not (token == "*") and not (token == "/"):
                stack.append(token)
            else:
                first = int(stack.pop())
                second = int(stack.pop())
                if token == "+":
                    stack.append(second + first)
                elif token == "-":
                    stack.append(second - first)
                elif token == "*":
                    stack.append(second * first)
                else:
                    stack.append(int(second / first))
            

        return stack.pop()

