class Solution(object):
    def uniquePaths(self, m, n):
        # bottom-up
        # dp = [[-1] * n for _ in range(m)]

        # for r in range(m):
        #     dp[r][0] = 1
        
        # for c in range(n):
        #     dp[0][c] = 1

        # for r in range(1,m):
        #     for c in range(1,n):
        #         dp[r][c] = dp[r-1][c] + dp[r][c-1]
        # return dp[m-1][n-1]

        # top-down
        memo = [[-1]*n for _ in range(m)]

        def dp(r,c):
            if r==0 or c==0:
                memo[r][c] = 1
            
            if memo[r][c] == -1:
                memo[r][c] = dp(r-1,c) + dp(r,c-1)

            return memo[r][c]
        return dp(m-1,n-1)
        

        