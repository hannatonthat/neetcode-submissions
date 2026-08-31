class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        grids = [0] * 9

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                
                val = int(board[i][j]) - 1
                if ((1 << val) & rows[i] or
                    (1 << val) & cols[j] or
                    (1 << val) & grids[((i // 3) * 3 + j // 3)]):
                    return False
                
                rows[i] |= (1 << val)
                cols[j] |= (1 << val)
                grids[((i // 3) * 3 + j // 3)] |= (1 << val)
            
        return True