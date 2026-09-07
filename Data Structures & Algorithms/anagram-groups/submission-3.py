class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        words_dict = dict()

        for i, word in enumerate(strs):
            
            word_counts = [0] * 26

            for char in word:
                word_counts[ord(char) - ord('a')] += 1
            
            dict_key = tuple(word_counts)

            if dict_key in words_dict:
                words_dict[dict_key].append(i)
            else:
                words_dict[dict_key] = [i]
    

        for indexes in words_dict.values():
            temp = []            
            for index in indexes:
                temp.append(strs[index])
            result.append(temp)

        return result

        # we are sorting to build something that's identical for all anagrams but different for non-anagrams
        # instead of doing this, we can ... 