class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # bottom up -- 49ms
        # n = len(cost)
        # dp=[-1]*(n+1)

        # dp[0]=0
        # dp[1]=0

        # for i in range(2,n+1):
        #     dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        # return dp[n]

        # top down -- 
        memo = {}
        n = len(cost)
        def dp(n):
            if n==1 or n==0 : return 0
            if n not in memo:
                memo[n] = min(dp(n-1)+cost[n-1] , dp(n-2)+cost[n-2])
            return memo[n]
        return dp(n)