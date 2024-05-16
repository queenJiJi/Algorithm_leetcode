class Solution(object):
    def coinChange(self, coins, amount):
        dp = [amount+1] * (amount+1)
        dp[0] =0 
        
        for a in range(amount+1):
            for coin in coins:
                if a-coin >= 0:
                    dp[a] = min(dp[a], 1+dp[a-coin])
        return dp[amount] if dp[amount]!=amount+1 else -1
        