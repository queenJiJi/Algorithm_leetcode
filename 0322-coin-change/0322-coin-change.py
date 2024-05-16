from collections import deque
class Solution(object):
    def coinChange(self, coins, amount):
        q= deque([(amount,0)])
        visited= set()
        while q:
            cur_amount, num_coin = q.popleft()
            
            if cur_amount == 0:
                return num_coin

            for coin in coins:
                next_coin = cur_amount - coin
                if next_coin not in visited and next_coin>=0:
                    q.append((next_coin, num_coin+1))
                    visited.add(next_coin)
        return -1