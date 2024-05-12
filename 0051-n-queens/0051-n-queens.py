class Solution(object):
    def solveNQueens(self, n):
        result = []
        cols= set()
        rightDiag=set()
        leftDiag=set()
        board=[['.']*n for _ in range(n)]
        def backtrack(row):
            if row == n:
                copy_row = [''.join(row) for row in board] 
                result.append(copy_row)
                return

            for col in range(n):
                if col in cols or (row+col) in leftDiag or (row-col) in rightDiag:
                    continue

                cols.add(col)
                rightDiag.add(row-col)
                leftDiag.add(row+col)
                board[row][col] = 'Q'
                backtrack(row+1)
                cols.remove(col)
                rightDiag.remove(row-col)
                leftDiag.remove(row+col)
                board[row][col] = '.'

        backtrack(0)
        return result