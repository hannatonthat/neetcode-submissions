class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        res, seen = set(), set()
        root = TrieNode()
        for w in words:
            root.addWord(w)

        def dfs(r, c, node, word):
            if (r >= rows or c >= cols or
                r < 0 or c < 0 or
                (r, c) in seen or
                board[r][c] not in node.children):
                return
            seen.add((r, c))
            word += board[r][c]
            node = node.children[board[r][c]]
            if node.endOfWord:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            
            seen.remove((r, c))
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")
        return list(res)