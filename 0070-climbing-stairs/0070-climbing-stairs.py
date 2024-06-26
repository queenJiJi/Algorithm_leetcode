class Solution(object):
    def climbStairs(self, n):
        # dp = [0] * (n+1)

        # dp[0] = 1
        # dp[1] = 1

        # for i in range(2,n+1):
        #     dp[i] = dp[i-1] + dp[i-2]

        # return dp[n]

        memo = [0] * (n+1)

        def dp(n):
            if n==0 or n==1:
                return memo[n] = 1

            memo[n] = dp(n-1)+ dp(n-2)
            return memo[n]
        return dp(n)

        
        



















        # top_down
        # memo = [-1] * (n+1)        

        # def dp(n):
        #     # base case
        #     if n==0 or n == 1:
        #         memo[n] = 1
            
        #     if memo[n] == -1:
        #         memo[n] = dp(n-1) + dp(n-2)
        #     return memo[n]
        # return dp(n)

        # bottom-up
        # dp = [-1] * (n+1)

        # dp[0] = 1
        # dp[1] = 1

        # for i in range(2,n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[n]