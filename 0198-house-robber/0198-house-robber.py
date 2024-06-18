class Solution(object):
    def rob(self, nums):
        n = len(nums)
        # bottom up
        # dp = [-1] * n

        # dp[0] = nums[0]

        # if n>1:
        #     dp[1] = max(nums[0], nums[1])

        #     for i in range(2,n):
        #         dp[i] = max(dp[i-2]+nums[i], dp[i-1])
            
        # return dp[n-1]
        
        # top-down
        memo={}

        def dp(n):
            if n==0:
                return nums[0]
            if n==1:
                return max(nums[0],nums[1])
            if n not in memo:
                memo[n] = max(dp(n-2)+nums[n], dp(n-1))
            return memo[n]
        return dp(n-1)
        