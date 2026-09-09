class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1): return False

        s1_counts, s2_counts = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1_char, s2_char = s1[i], s2[i]
            s1_counts[ord(s1_char) - ord('a')] += 1
            s2_counts[ord(s2_char) - ord('a')] += 1

        if s1_counts == s2_counts: return True

        for i in range(1, (len(s2) - len(s1)) + 1):
            prev_char = s2[i - 1]
            new_char = s2[i + (len(s1) - 1)]

            s2_counts[ord(prev_char) - ord('a')] -= 1
            s2_counts[ord(new_char) - ord('a')] += 1

            if s1_counts == s2_counts: return True

        return False
