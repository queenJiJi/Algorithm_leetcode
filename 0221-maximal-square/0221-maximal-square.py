class Solution(object):
    def maximalSquare(self, matrix):
        # top-down
        rows = len(matrix)
        cols = len(matrix[0])
        memo ={}

        def dp(r,c):
            if r>=rows or c>=cols:
                return 0
            
            if (r,c) not in memo:
                down = dp(r+1,c)
                right = dp(r,c+1)
                diag = dp(r+1,c+1)

                memo[(r,c)] = 0
                if matrix[r][c] == '1':
                    memo[(r,c)] = min(down,right,diag)+1
            return memo[(r,c)]
        dp(0,0)
        return max(memo.values())**2

                
        