class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_map = [0] * 26
        s2_map = [0] * 26

        l = 0
        for r in range(len(s1)):
            s1_map[ord(s1[r]) - ord("a")] += 1
            s2_map[ord(s2[r]) - ord("a")] += 1

        if s1_map == s2_map:
                return True

        for r in range(len(s1), len(s2), 1):
            s2_map[ord(s2[l]) - ord("a")] -= 1
            l += 1
            s2_map[ord(s2[r]) - ord("a")] += 1
            if s1_map == s2_map:
                return True

        return False