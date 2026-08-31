class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        tMap = {}

        for c in t:
            tMap[c] = 1 + tMap.get(c, 0)
        
        sMap = {}
        l = 0
        have, need = 0, len(tMap)
        res = [-1, -1]
        resLen = float("inf")

        for r in range(len(s)):
            c = s[r]
            sMap[c] = 1 + sMap.get(c, 0)
            
            if c in tMap and sMap[c] == tMap[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                sMap[s[l]] -= 1
                if s[l] in tMap and sMap[s[l]] < tMap[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l:r + 1] if resLen != float("inf") else ""
                
                