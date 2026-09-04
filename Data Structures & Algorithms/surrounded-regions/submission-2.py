class Solution:
    def solve(self, board: List[List[str]]) -> None:
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if (r < 0 or c < 0 or 
                r >= rows or c >= cols or
                board[r][c] != "O"):
                return
            board[r][c] = "T"
            for dr, dc in dirs:
                dfs(r + dr, c + dc)
        
        for r in range(rows):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][cols - 1] == "O":
                dfs(r, cols - 1)
        
        for c in range(cols):
            if board[0][c] == "O":
                dfs(0, c)
            if board[rows - 1][c] == "O":
                dfs(rows - 1, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "T":
                    board[r][c] = "O"