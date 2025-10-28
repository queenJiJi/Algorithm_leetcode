class Solution(object):
    def solveNQueens(self, n):
        answer = []
        board= [["."] * n for _ in range(n)]
        c_set, r_diag, l_diag = set(), set(), set()
        
        def backtrack(row):
            if row == n:
                answer.append([''.join(row) for row in board])
                return

            for c in range(n):
                if c in c_set or (row+c) in l_diag or (row-c) in r_diag:
                    continue
                
                c_set.add(c)
                l_diag.add(row+c)
                r_diag.add(row-c)
                board[row][c] = 'Q'
                backtrack(row+1)
                c_set.remove(c)
                l_diag.remove(row+c)
                r_diag.remove(row-c)
                board[row][c] = '.'
        backtrack(0)
        return answer


        