class Solution(object):
    def rob(self, nums):
        n = len(nums)
        dp=[0]*n

        dp[0] = nums[0]

        if n>1: 
            dp[1] = max(nums[0],nums[1])

            for i in range(2,n):
                dp[i] = max(dp[i-2]+nums[i], dp[i-1])
            return dp[n-1]
    