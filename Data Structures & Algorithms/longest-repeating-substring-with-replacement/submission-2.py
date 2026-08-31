class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = defaultdict(int)

        l = 0
        res = 0
        maxFreq = 0

        for r in range(len(s)):
            freq_map[s[r]] += 1
            maxFreq = max(maxFreq, freq_map[s[r]])
            while (r - l + 1) - maxFreq > k:
                freq_map[s[l]] -= 1
                l += 1
            res = max(res, (r - l + 1))

        return res