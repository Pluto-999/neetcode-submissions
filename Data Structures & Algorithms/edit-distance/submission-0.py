class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}

        def search(i, j):
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            if i == len(word1) and j == len(word2):
                return 0
            
            # insert the remaining
            if i == len(word1) and j != len(word2):
                dp[(i, j)] = len(word2) - j
                return dp[(i, j)]

            # delete the remaining
            if j == len(word2) and i != len(word1):
                return len(word1) - i
                dp[(i, j)] = len(word1) - i
                return dp[(i, j)]

            if word1[i] == word2[j]:
                dp[(i, j)] = 0 + search(i + 1, j + 1)
                return dp[(i, j)]
            
            # insert = j + 1 ; delete = i + 1 ; replace = i + 1, j + 1

            else:
                dp[(i, j)] = 1 + min(search(i, j + 1), search(i + 1, j), search(i + 1, j + 1))
                return dp[(i, j)]


        return search(0, 0)