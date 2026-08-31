class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
            
        s1_map = [0] * 26
        s2_map = [0] * 26

        for i in range(len(s1)):
            s1_map[ord(s1[i]) - ord('a')] += 1
            s2_map[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if s1_map[i] == s2_map[i]:
                matches += 1
        
        if matches == 26:
            return True
        
        l = 0
        for r in range(len(s1), len(s2)):
            i = ord(s2[r]) - ord('a')
            s2_map[i] += 1
            if s1_map[i] == s2_map[i]:
                matches += 1
            elif (s1_map[i] + 1) == s2_map[i]:
                matches -= 1
            j = ord(s2[l]) - ord('a')
            s2_map[j] -= 1
            if s1_map[j] == s2_map[j]:
                matches += 1
            elif (s1_map[j] - 1) == s2_map[j]:
                matches -= 1
            if matches == 26:
                return True
            l += 1

        return False