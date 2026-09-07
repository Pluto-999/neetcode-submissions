class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        words_dict = dict()

        for i, word in enumerate(strs):
            sorted_word = "".join(sorted(word))
            if sorted_word in words_dict:
                words_dict[sorted_word].append(i)
            else:
                words_dict[sorted_word] = [i]

        for indexes in words_dict.values():
            temp = []            
            for index in indexes:
                temp.append(strs[index])
            result.append(temp)

        return result
