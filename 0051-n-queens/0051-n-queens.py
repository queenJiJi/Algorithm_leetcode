class Solution(object):
    def solveNQueens(self, n):
        answer = []
        board= [['.' for _ in range(n)] for _ in range(n)]
        c_set,rd,ld = set(),set(),set()

        def backtrack(row):
            
            if row == n:
                copying = [''.join(row) for row in board]
                answer.append(copying)
                return

            for col in range(n):
                if col in c_set or (row+col) in rd or (row-col) in ld:
                    continue

                c_set.add(col)
                rd.add(row+col)
                ld.add(row-col)
                board[row][col] = 'Q'
                backtrack(row+1)
                c_set.remove(col)
                rd.remove(row+col)
                ld.remove(row-col)
                board[row][col] = '.'
            
        backtrack(0)
        return answer
