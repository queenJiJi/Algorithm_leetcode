class Solution(object):
    def solveNQueens(self, n):
        result = []
        board = [['.']*n for _ in range(n)]
        cols,leftDiag,rightDiag = set(),set(),set()

        def backtrack(row):
            if row == n:
                copy_row = [''.join(r) for r in board]
                result.append(copy_row)
                return
            
            for col in range(n):
                if (col in cols or (row-col) in leftDiag or (row+col) in rightDiag):
                    continue
                
                cols.add(col)
                leftDiag.add((row-col))
                rightDiag.add((row+col))
                board[row][col] = 'Q'
                backtrack(row+1)
                cols.remove(col)
                leftDiag.remove((row-col))
                rightDiag.remove((row+col))
                board[row][col] = '.'
            return result
        return backtrack(0)
                