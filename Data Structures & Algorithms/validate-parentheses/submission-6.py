class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        stack = []
        bracket_map = {
            "}": "{",
            "]": "[",
            ")": "(",
        }

        for c in s:
            if c not in bracket_map:
                stack.append(c)
            else:
                if not stack or stack[-1] != bracket_map[c]:
                    return False
                stack.pop()
        
        return stack == []