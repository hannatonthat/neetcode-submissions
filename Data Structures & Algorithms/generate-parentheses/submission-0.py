class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subset = []
        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(subset))
                return
            if openN < n:
                subset.append("(")
                backtrack(openN + 1, closedN)
                subset.pop()
            if closedN < openN:
                subset.append(")")
                backtrack(openN, closedN + 1)
                subset.pop()
        backtrack(0, 0)
        return res