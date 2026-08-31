class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or t == "":
            return ""

        t_map = defaultdict(int)
        s_map = defaultdict(int)

        for c in t:
            t_map[c] += 1

        res = float("inf")
        resIndex = [-1, -1]
        l = 0
        have, need = 0, len(t_map)

        for r in range(len(s)):
            s_map[s[r]] += 1

            if s[r] in t_map and s_map[s[r]] == t_map[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < res:
                    res = r - l + 1
                    resIndex = [l, r]

                s_map[s[l]] -= 1
                if s[l] in t_map and s_map[s[l]] < t_map[s[l]]:
                    have -= 1
                l += 1

        l, r = resIndex
        return s[l:r + 1] if resIndex != [-1, -1] else ""