from collections import deque
class Solution(object):
    def coinChange(self, coins, amount):
      
        q = deque()
        q.append((amount,0))
        visited=set()
        while q:
            cur_amount,num_coins = q.popleft()
            visited.add(cur_amount)

            if cur_amount == 0:
                return num_coins

            for coin in coins:
                next_amount = cur_amount-coin
                if next_amount >= 0 and next_amount not in visited:
                    visited.add(next_amount)
                    q.append((next_amount,num_coins+1)) 

        return -1