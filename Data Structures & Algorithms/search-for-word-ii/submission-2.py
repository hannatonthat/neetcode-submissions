class Node:
    def __init__(self, val=None):
        self.val = val
        self.end = False
        self.children = defaultdict(list)

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node(c)
            curr = curr.children[c]
        curr.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for w in words:
            trie.insert(w)
        
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        rows, cols = len(board), len(board[0])
        res, subset = set(), []
        seen = set()

        def dfs(r, c, curr):
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                board[r][c] not in curr.children or
                (r, c) in seen):
                return
                    
            seen.add((r, c))
            subset.append(board[r][c])
            nxt = curr.children[board[r][c]]

            if nxt.end:
                res.add("".join(subset.copy()))

            for dr, dc in dirs:
                if (r + dr, c + dc) not in seen:
                    dfs(r + dr, c + dc, nxt)
            subset.pop()
            seen.remove((r, c))
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie.root)
        
        return list(res)