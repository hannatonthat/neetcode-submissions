class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            wordLen = int(s[i:j])
            word = s[j + 1:j + wordLen + 1]
            res.append(word)
            i = j + wordLen + 1
        
        return res