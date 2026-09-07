class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}

        for string in strs:
            sorted_string = ''.join(sorted(string))
            if sorted_string in my_dict:
                my_dict[sorted_string].append(string)
            else:
                my_dict[sorted_string] = [string]

        result = []

        for value in my_dict.values():
            result.append(value)

        return result
        