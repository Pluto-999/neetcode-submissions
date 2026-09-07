class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        my_dict = {}

        for s in s1:
            if s in my_dict:
                my_dict[s] = my_dict.get(s) + 1
            else:
                my_dict[s] = 1

        second_dict = {}

        inner = 0
        
        for right, s in enumerate(s2):
            if s not in my_dict:
                continue
            else:
                while (inner < len(s1) and right + inner < len(s2)):
                    each_char = s2[right + inner]
                    if each_char in second_dict:
                        second_dict[each_char] = second_dict.get(each_char) + 1
                    else:
                        second_dict[each_char] = 1
                    inner += 1
                
                not_possible = False

                for key in my_dict:
                    if key not in second_dict:
                        not_possible = True
                        break
                    if my_dict[key] != second_dict[key]:
                        not_possible = True
                        break
                
                if not not_possible:
                    return True
                else:
                    inner = 0
                    second_dict.clear()

        return False

        


        

        


