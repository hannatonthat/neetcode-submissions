class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqMap = {}
        maxFreq = 0
        
        res = 0
        l = 0
        for r in range(len(s)):
            freqMap[s[r]] = 1 + freqMap.get(s[r], 0)
            maxFreq = max(maxFreq, freqMap[s[r]])

            while (r - l + 1) - maxFreq > k:
                freqMap[s[l]] -= 1
                l += 1           
            res = max(res, (r - l + 1))

        return res