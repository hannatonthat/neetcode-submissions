class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1

        while top < bot:
            m = (top + bot) // 2
            if target < matrix[m][0]:
                bot = m - 1
            elif target > matrix[m][-1]:
                top = m + 1
            else:
                break
        
        if top > bot:
            return False

        row = (top + bot) // 2

        l, r = 0, len(matrix[0]) - 1

        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return False
