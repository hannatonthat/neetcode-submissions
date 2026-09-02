class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        res, subset = [], []
        def dfs(i):
            if i >= len(s):
                res.append(subset.copy())
            
            for j in range(i, len(s)):
                if isPalindrome(i, j):
                    subset.append(s[i:j + 1])
                    dfs(j + 1)
                    subset.pop()
        dfs(0)
        return res