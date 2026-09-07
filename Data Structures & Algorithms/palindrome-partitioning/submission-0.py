class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        result = []
        # current = []

        def is_palindrome(string):
            left = 0
            right = len(string) - 1
            while left < right:
                if string[left] != string[right]:
                    return False
                left += 1
                right -= 1
            return True
            

        def search(arr, index):
            if index == len(s):
                for string in arr:
                    if not is_palindrome(string):
                        return
                result.append(arr[:])
                return

            # separate (i.e. new list item)
            arr.append(s[index])
            search(arr, index + 1)
            arr.pop()

            # together (i.e. add char to last list item)
            last_index = len(arr) - 1
            arr[last_index] = arr[last_index] + s[index]
            
            search(arr, index + 1)



        first_element = s[0]
        search([first_element], 1)
        return result