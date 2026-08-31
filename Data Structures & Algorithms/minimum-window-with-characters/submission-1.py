class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map = Counter(t)
        have = 0
        need = len(t_map)
        s_map = {}
        resLen = float("inf")
        resIdx = [-1, -1]

        l, r = 0, 0
        while r < len(s):
            s_map[s[r]] = 1 + s_map.get(s[r], 0)
            if s_map[s[r]] == t_map[s[r]]:
                have += 1
            while have == need:
                if (r - l + 1) < resLen:
                    resLen = (r - l + 1)
                    resIdx = [l, r]
                s_map[s[l]] -= 1
                if (s_map[s[l]] + 1) == t_map[s[l]]:
                    have -= 1
                l += 1
            r += 1
        
        l, r = resIdx
        return s[l:r + 1]