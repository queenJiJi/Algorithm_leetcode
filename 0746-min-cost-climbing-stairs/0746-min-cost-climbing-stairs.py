class Solution(object):
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        dp = [float('inf')] * (n+1)

        dp[0] = 0
        dp[1] = 0
        
        for i in range(2,n+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])

        return dp[n]















        # n = len(cost)
       # top-down
        # memo = {}

        # def dp(n):
        #     if n==0 or n==1:
        #         return 0
            
        #     if n not in memo:
        #         memo[n] = min(dp(n-1)+cost[n-1], dp(n-2)+cost[n-2])
        #     return memo[n]
        # return dp(n)
        
        # bottom-up
        dp = [-1] * (n+1)

        dp[0] = 0
        dp[1] = 0

        for i in range(2,n+1):
            dp[i] = min(dp[i-1]+cost[i-1] , dp[i-2]+cost[i-2])
        return dp[n]
        


        