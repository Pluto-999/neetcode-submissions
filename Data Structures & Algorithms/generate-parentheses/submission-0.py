class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        self.result = []

        def recurse(left_count, right_count, current):
            if left_count == right_count and left_count == n:
                self.result.append(current)
                return
            
            if left_count < n:
                recurse(left_count + 1, right_count, current + "(")
                
            if right_count < left_count:
                recurse(left_count, right_count + 1, current + ")")

        recurse(0, 0, "")
        return self.result