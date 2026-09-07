class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits) == 0:
            return []

        my_dict = {}
        my_dict["2"] = "abc"
        my_dict["3"] = "def"
        my_dict["4"] = "ghi"
        my_dict["5"] = "jkl"
        my_dict["6"] = "mno"
        my_dict["7"] = "pqrs"
        my_dict["8"] = "tuv"
        my_dict["9"] = "wxyz"

        result = []

        def search(index, current):
            if len(current) == len(digits):
                result.append(current)
                return

            number = digits[index]
            options = my_dict[number]
            for i in range(0, len(options)):
                current += options[i]
                search(index + 1, current)
                current = current[:-1]
    
            


        search(0, "")
        return result