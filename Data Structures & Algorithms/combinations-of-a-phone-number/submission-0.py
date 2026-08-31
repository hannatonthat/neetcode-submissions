class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hash_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []

        def backtrack(i, s):
            if len(s) == len(digits):
                res.append(s)
                return
            for c in hash_map[digits[i]]:
                backtrack(i + 1, s + c)
        
        if digits:
            backtrack(0, "")
        
        return res            