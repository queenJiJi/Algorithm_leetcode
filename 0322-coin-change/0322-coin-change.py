class Solution(object):
    def coinChange(self, coins, amount):
        dp = [float('inf')] * (amount+1)

        dp[0] = 0

        for a in range(1,amount+1):
            for c in coins:
                if a-c>=0:
                    dp[a] = min(dp[a],dp[a-c]+1)
        return -1 if dp[amount] == float('inf') else dp[amount]

    