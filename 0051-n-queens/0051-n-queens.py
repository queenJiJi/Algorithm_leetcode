class Solution(object):
    def solveNQueens(self, n):
        c, ld,rd  = set(),set(),set()
        answer = []
        board = [['.']*n for _ in range(n)]
        def backtrack(row):
            if row == n:
                answer.append([''.join(row) for row in board])
                return

            for col in range(n):
                if col in c or (col+row) in ld or (col-row) in rd:
                    continue

                c.add(col)
                ld.add(col+row)
                rd.add(col-row)
                board[row][col] = 'Q'
                backtrack(row+1)
                c.remove(col)
                ld.remove(col+row)
                rd.remove(col-row)
                board[row][col] = '.'
        backtrack(0)
        return answer
                 
        